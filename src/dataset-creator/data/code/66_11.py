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
            'absolute_difference': abs_diff,
            'signed_difference': signed_diff,
            'percentage_variance': pct_variance
        }
def analyze_multiple_pairs(pairs: List[Tuple[float, float]]) -> dict:
    analyzer = WeightAnalyzer()
    results_list = []
    for p1, p2 in pairs:
        metrics = analyzer.compute_metrics(p1, p2)
        results_list.append(metrics)
    return {
        'results': results_list,
        'total_pairs_processed': len(results_list),
        'overall_abs_diff_sum': sum(r['absolute_difference'] for r in results_list),
        'max_signed_diff': max((r['signed_difference'] if isinstance(r['percentage_variance'], float) else 0 
                              for r in results_list)),
    }
if __name__ == '__main__':
    sample_pairs = [
        (15, 20),
        (100.5, 98.3),
        (-5, -10),
        (75, 0)
    ]
    final_output = analyze_multiple_pairs(sample_pairs)
    print(final_output)