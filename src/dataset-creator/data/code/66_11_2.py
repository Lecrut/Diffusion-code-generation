import statistics as stats
class WeightAnalyzer:
    def __init__(self):
        self.pairs = []
    def add_pair(self, w1, w2):
        self.pairs.append((w1, w2))
    def compute_absolute_difference(self, pair_index):
        if 0 <= pair_index < len(self.pairs):
            return abs(self.pairs[pair_index][0] - self.pairs[pair_index][1])
        raise IndexError("Pair index out of range")
    def compute_signed_difference(self, pair_index):
        if 0 <= pair_index < len(self.pairs):
            return self.pairs[pair_index][0] - self.pairs[pair_index][1]
        raise IndexError("Pair index out of range")
    def compute_percentage_variance(self, pair_index):
        w1 = self.pairs[pair_index][0]
        w2 = self.pairs[pair_index][1]
        if abs(w2) > 0:
            return ((w1 - w2) / w2) * 100
        raise ValueError("Division by zero")
    def batch_compute(self, pair_indices):
        results = {}
        for idx in sorted(pair_indices):
            absolute_diff = self.compute_absolute_difference(idx)
            signed_diff = self.compute_signed_difference(idx)
            pct_var = self.compute_percentage_variance(idx)
            results[idx] = (absolute_diff, signed_diff, pct_var)
        return results
if __name__ == '__main__':
    analyzer = WeightAnalyzer()
    sample_pairs = [
        (100.5, 98.2),
        (75.0, 80.3),
        (200.0, 195.5)
    ]
    for w1, w2 in sample_pairs:
        analyzer.add_pair(w1, w2)
    indices = [0, 1]
    results = analyzer.batch_compute(indices)
    print("Batch Analysis Results:")
    for idx, (abs_diff, signed_diff, pct_var) in sorted(results.items()):
        pair_idx = list(sample_pairs).index((sample_pairs[idx][0], sample_pairs[idx][1])) if isinstance(idx, int) else None
        print(f"Index {idx}: Absolute={abs_diff:.2f}, Signed={signed_diff:+.2f}, Variance%={pct_var:+.2f}%")
    single_results = analyzer.compute_absolute_difference(0)
    print(f"Single check (idx 0 abs): {single_results}")