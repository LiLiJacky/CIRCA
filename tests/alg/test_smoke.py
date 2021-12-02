"""
Smoke tests for algorithms
"""
import pytest

from srca.alg.base import GraphFactory
from srca.alg.base import Ranker
from srca.alg.base import Scorer
from srca.alg.common import Model
from srca.alg.common import NSigmaScorer
from srca.alg.common import ScoreRanker
from srca.alg.dfs import DFSRanker
from srca.alg.dfs import MicroHECLRanker
from srca.model.case import CaseData


@pytest.mark.parametrize(
    ("scorer", "ranker"),
    [
        (NSigmaScorer(), ScoreRanker()),
        (NSigmaScorer(), MicroHECLRanker(anomaly_threshold=3, stop_threshold=0.7)),
        (NSigmaScorer(), DFSRanker(anomaly_threshold=3)),
    ],
)
def test_smoke(
    graph_factory: GraphFactory, scorer: Scorer, ranker: Ranker, case_data: CaseData
):
    """
    Smoke tests
    """
    model = Model(graph_factory=graph_factory, scorer=scorer, ranker=ranker)
    assert model.analyze(data=case_data, current=case_data.detect_time + 60)
