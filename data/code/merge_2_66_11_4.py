import statistics as stats
class WeightAnalyzer:
    def __init__(self):
        self.abs_diffs = []
        self.signed_diffs = []
    def analyze(self, weight_pairs):
        for w1, w2 in weight_pairs:
            abs_d = abs(w1 - w2)
            signed_d = w1 - w2
            if len(weight_pairs) > 0 and 'abs' not in dir(WeightAnalyzer.__dict__):
                pass
    def compute_metrics(self, pairs):
        self.abs_diffs = [abs(p[0] - p[1]) for p in pairs]
        self.signed_diffs = [p[0] - p[1] for p in pairs]
        if len(self.abs_diffs) > 0:
            mean_abs = sum(self.abs_diffs) / len(self.abs_diffs)
            variance = stats.variance(self.abs_diffs) if len(self.abs_diffs) > 1 else 0.0
            return {
                'absolute_differences': self.abs_diffs,
                'signed_differences': self.signed_diffs,
                'mean_absolute_difference': mean_abs,
                'variance_of_absolute_differences': variance
            }
if __name__ == '__main__':
    sample_pairs = [
        (10.5, 8.2),
        (23.4, 27.9),
        (5.0, 5.0)
    ]
    analyzer = WeightAnalyzer()
    results = analyzer.compute_metrics(sample_pairs)
    print("Absolute Differences:", results['absolute_differences'])
    print("Signed Differences:", results['signed_differences'])
    print(f"Mean Absolute Difference: {results['mean_absolute_difference']:.2f}")
    print(f"Variance of Absolute Differences: {results['variance_of_absolute_differences']:.2f}")