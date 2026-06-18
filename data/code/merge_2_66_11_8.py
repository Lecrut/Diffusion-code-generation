import math
from typing import List, Tuple
class WeightAnalyzer:
    def compute_metrics(self, pair1: float, pair2: float) -> dict:
        abs_diff = abs(pair1 - pair2)
        signed_diff = pair1 - pair2
        if pair2 == 0:
            pct_variance = None
        else:
            pct_variance = ((pair1 - pair2) / pair2) * 100
        return {
            "absolute_difference": abs_diff,
            "signed_difference": signed_diff,
            "percentage_variance": pct_variance
        }
def process_multiple_pairs(pairs: List[Tuple[float, float]]) -> dict:
    analyzer = WeightAnalyzer()
    results = []
    for p1, p2 in pairs:
        metrics = analyzer.compute_metrics(p1, p2)
        results.append(metrics)
    return {
        "results": results,
        "total_pairs_processed": len(results),
        "max_absolute_difference": max([r["absolute_difference"] for r in results]) if results else 0.0
    }
if __name__ == '__main__':
    sample_data = [
        (100.5, 98.2),
        (75.0, 80.3),
        (200.0, 150.0)
    ]
    final_output = process_multiple_pairs(sample_data)
    print(final_output)