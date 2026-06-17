import math
class WeightAnalyzer:
    def compute_metrics(self, pair1, pair2):
        diff_abs = abs(pair1 - pair2)
        diff_signed = pair1 - pair2
        if pair2 == 0:
            variance_pct = float('inf') if pair1 > 0 else (-float('inf'), None)[pair1 < 0] or (None, None)
        elif pair2 != 0:
            variance_pct = ((pair1 - pair2) / abs(pair2)) * 100
        return {
            'absolute_difference': diff_abs,
            'signed_difference': diff_signed,
            'percentage_variance': variance_pct if not (variance_pct == float('inf') or variance_pct is None) else "Undefined"
        }
def main():
    pairs = [
        ([10.5], [20.3]),
        ([-5.0], [-8.7]),
        ([100], [90])
    ]
    analyzer = WeightAnalyzer()
    for i, (w_list_1, w_list_2) in enumerate(pairs):
        if len(w_list_1) == 1 and len(w_list_2) == 1:
            result = analyzer.compute_metrics(w_list_1[0], w_list_2[0])
            print(f"Pair {i+1}:")
            print(f"Absolute Difference: {result['absolute_difference']}")
            print(f"Signed Difference: {result['signed_difference']}")
            if isinstance(result['percentage_variance'], str):
                print(f"Percentage Variance: Undefined (Division by zero or invalid input)")
            else:
                print(f"Percentage Variance: {result['percentage_variance']}%")
if __name__ == '__main__':
    main()