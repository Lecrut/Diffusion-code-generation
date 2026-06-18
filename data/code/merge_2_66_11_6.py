import math
from typing import List, Tuple
class WeightAnalyzer:
    def compute_metrics(self, pairs: List[Tuple[float, float]]) -> dict:
        results = []
        for w1, w2 in pairs:
            abs_diff = abs(w1 - w2)
            signed_diff = w1 - w2
            if w2 != 0:
                pct_variance = (abs_diff / w2) * 100.0
            else:
                pct_variance = float('inf') if abs_diff > 0 else 0.0
            results.append({
                'pair': [w1, w2],
                'absolute_difference': round(abs_diff, 4),
                'signed_difference': signed_diff,
                'percentage_variance': round(pct_variance, 4) if pct_variance != float('inf') else "Infinity"
            })
        return results
if __name__ == '__main__':
    sample_pairs = [
        (10.5, 23.7),
        (0.0, 5.0),
        (-4.2, -8.9)
    ]
    analyzer = WeightAnalyzer()
    output = analyzer.compute_metrics(sample_pairs)
    for item in output:
        print(f"Pair {item['pair']}:")
        print(f"Absolute Difference: {item['absolute_difference']}")
        print(f"Signed Difference: {item['signed_difference']}")
        if isinstance(item['percentage_variance'], str):
            print(f"Percentage Variance: {item['percentage_variance']}")
        else:
            print(f"Percentage Variance: {item['percentage_variance']}%")