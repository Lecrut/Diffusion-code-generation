import math
class WeightAnalyzer:
    def __init__(self):
        self.abs_diffs = []
        self.signed_diffs = []
        self.percent_variances = []
    def analyze(self, weight_pairs):
        for w1, w2 in weight_pairs:
            abs_d = abs(w1 - w2)
            signed_d = w1 - w2
            if w2 != 0:
                pct_v = (abs_d / w2) * 100
            else:
                pct_v = float('inf')
            self.abs_diffs.append(abs_d)
            self.signed_diffs.append(signed_d)
            self.percent_variances.append(pct_v)
    def get_results(self):
        return {
            'absolute_differences': sum(self.abs_diffs),
            'signed_difference_sum': sum(self.signed_diffs),
            'total_variance_percentage': round(sum(self.percent_variances), 2) if self.percent_variances else None
        }
if __name__ == '__main__':
    sample_pairs = [
        (10, 5),
        (20, 30),
        (100, 98),
        (50, 50)
    ]
    analyzer = WeightAnalyzer()
    analyzer.analyze(sample_pairs)
    results = analyzer.get_results()
    print(f"Total Absolute Difference: {results['absolute_differences']}")
    print(f"Sum of Signed Differences: {results['signed_difference_sum']}")
    print(f"Total Percentage Variance: {results['total_variance_percentage']}%")