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
    results_list = []
    for p1, p2 in pairs:
        metrics = analyzer.compute_metrics(p1, p2)
        results_list.append(metrics)
    return {
        "results": results_list,
        "total_pairs_processed": len(results_list),
        "average_absolute_difference": sum(r["absolute_difference"] for r in results_list) / len(results_list) if results_list else 0.0
    }
if __name__ == '__main__':
    sample_data = [
        (100, 50),
        (200, 300),
        (75, 75),
        (10, 0)
    ]
    final_output = process_multiple_pairs(sample_data)
    print(f"Total pairs processed: {final_output['total_pairs_processed']}")
    print(f"Average absolute difference: {final_output['average_absolute_difference']:.2f}")
    for i, result in enumerate(final_output["results"], 1):
        abs_diff = result.get("absolute_difference", "N/A")
        signed_diff = result.get("signed_difference", "N/A")
        pct_var = f"{result.get('percentage_variance', 'N/A'):.2f}%" if isinstance(result.get('percentage_variance'), float) else "N/A"
        print(f"\nPair {i}: ({sample_data[i-1][0]}, {sample_data[i-1][1]})")
        print(f"  Absolute Difference: {abs_diff}")
        print(f"  Signed Difference: {signed_diff}")
        print(f"  Percentage Variance: {pct_var}")