import numpy as np
class DistributionComparator:
    def __init__(self):
        self.data_a = None
        self.data_b = None
    def load_data(self, a=None, b=None):
        if a is not None and b is not None:
            self.data_a = np.array(a)
            self.data_b = np.array(b)
    def analyze_distribution(self):
        if self.data_a is None or self.data_b is None:
            raise ValueError("Data must be loaded before analysis.")
        stats_a = {
            'mean': float(np.mean(self.data_a)),
            'median': float(np.median(self.data_a)),
            'std_dev': float(np.std(self.data_a, ddof=0)),
            'min_val': float(np.min(self.data_a)),
            'max_val': float(np.max(self.data_a))
        }
        stats_b = {
            'mean': float(np.mean(self.data_b)),
            'median': float(np.median(self.data_b)),
            'std_dev': float(np.std(self.data_b, ddof=0)),
            'min_val': float(np.min(self.data_b)),
            'max_val': float(np.max(self.data_b))
        }
        return stats_a, stats_b
    def compute_correlation_matrix(self):
        if self.data_a is None or self.data_b is None:
            raise ValueError("Data must be loaded before analysis.")
        corr = np.corrcoef(self.data_a.reshape(-1, 1), self.data_b.reshape(-1, 1))
        return float(corr[0][1]) if len(corr) > 1 else 0.0
    def generate_report(self):
        stats_a, stats_b = self.analyze_distribution()
        report_lines = [
            "Dataset A Statistics:",
            f"Mean: {stats_a['mean']:.4f}",
            f"Median: {stats_a['median']:.4f}",
            f"Std Deviation: {stats_a['std_dev']:.4f}",
            f"Range: [{stats_a['min_val']}, {stats_a['max_val']}]",
            "Dataset B Statistics:",
            f"Mean: {stats_b['mean']:.4f}",
            f"Median: {stats_b['median']:.4f}",
            f"Std Deviation: {stats_b['std_dev']:.4f}",
            f"Range: [{stats_b['min_val']}, {stats_b['max_val']}]",
            "Comparison Metrics:",
            f"Covariance Matrix Element (A, B): {self.compute_correlation_matrix():.4f}"
        ]
        return "\n".join(report_lines)
if __name__ == '__main__':
    sample_data_a = [10, 25, 30, 45, 60]
    sample_data_b = [8, 27, 32, 48, 59]
    comparator = DistributionComparator()
    try:
        comparator.load_data(sample_data_a, sample_data_b)
        report = comparator.generate_report()
        print(report)
        if len(comparator.data_a) > 1 and len(comparator.data_b) > 1:
            corr_val = float(np.corrcoef(comparator.data_a.reshape(-1, 1), comparator.data_b.reshape(-1, 1))[0][1])
            print(f"\nCorrelation Coefficient (Pearson): {corr_val:.4f}")
    except Exception as e:
        print(f"Error during analysis: {e}")