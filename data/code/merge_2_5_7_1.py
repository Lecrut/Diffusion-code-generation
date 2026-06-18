import numpy as np
class DistributionComparator:
    def __init__(self):
        self.data1 = None
        self.data2 = None
    def load_data(self, dataset_1: list, dataset_2: list) -> None:
        self.data1 = np.array(dataset_1, dtype=float)
        self.data2 = np.array(dataset_2, dtype=float)
    def compute_basic_stats(self) -> dict:
        stats = {}
        if len(self.data1.shape) == 0 or len(self.data2.shape) == 0:
            self.data1 = np.array([self.data1])
            self.data2 = np.array([self.data2])
        stats['mean_1'] = float(np.mean(self.data1))
        stats['std_1'] = float(np.std(self.data1, ddof=0))
        if len(self.data2.shape) == 0:
            self.data2 = np.array([self.data2])
        stats['mean_2'] = float(np.mean(self.data2))
        stats['std_2'] = float(np.std(self.data2, ddof=0))
        return stats
    def compute_correlation_matrix(self) -> dict:
        if len(self.data1.shape) == 0 or len(self.data2.shape) == 0:
            self.data1 = np.array([self.data1])
            self.data2 = np.array([self.data2])
        corr_matrix = {}
        flat_1 = self.data1.flatten() if self.data1.ndim > 1 else self.data1
        flat_2 = self.data2.flatten() if self.data2.ndim > 1 else self.data2
        if len(flat_1) != len(flat_2):
            raise ValueError("Datasets must have the same length for correlation calculation.")
        corr_matrix['pearson'] = float(np.corrcoef(flat_1, flat_2)[0, 1])
        return {k: v for k, v in corr_matrix.items() if not np.isnan(v)}
    def compute_distribution_metrics(self) -> dict:
        metrics = {}
        self.data1 = np.atleast_1d(np.asarray(self.data1))
        self.data2 = np.atleast_1d(np.asarray(self.data2))
        if len(self.data1) < 3 or len(self.data2) < 3:
            raise ValueError("Datasets must contain at least 3 elements for skewness/kurtosis.")
        metrics['skewness_1'] = float(np.skew(self.data1, bias=False))
        metrics['excess_kurtosis_1'] = float(np.kurtosis(self.data1, fisher=True, bias=False))
        if len(self.data2) >= 3:
            metrics['skewness_2'] = float(np.skew(self.data2, bias=False))
            metrics['excess_kurtosis_2'] = float(np.kurtosis(self.data2, fisher=True, bias=False))
        return {k: v for k, v in metrics.items() if not np.isnan(v)}
def main():
    dataset_a = [10.5, 12.3, 9.8, 11.2, 13.1, 10.9]
    dataset_b = [14.2, 16.7, 15.1, 17.3, 14.8, 16.2]
    comparator = DistributionComparator()
    try:
        assert len(dataset_a) == len(dataset_b), "Input datasets must have equal length."
        comparator.load_data(dataset_a, dataset_b)
        basic_stats = comparator.compute_basic_stats()
        distribution_metrics = comparator.compute_distribution_metrics()
        correlation_matrix = comparator.compute_correlation_matrix()
        print("=== Distribution Comparison Report ===")
        print(f"Dataset A: {dataset_a}")
        print(f"Dataset B: {dataset_b}")
        print("\n--- Basic Statistics ---")
        print(f"A Mean: {basic_stats['mean_1']:.4f}, Std Dev: {basic_stats['std_1']:.4f}")
        print(f"B Mean: {basic_stats['mean_2']:.4f}, Std Dev: {basic_stats['std_2']:.4f}")
        if 'pearson' in correlation_matrix:
            corr = correlation_matrix['pearson']
            label = "Strong" if abs(corr) > 0.7 else ("Moderate" if abs(corr) > 0.3 else "Weak")
            print(f"Pearson Correlation (A vs B): {corr:.4f} ({label})")
        print("\n--- Distribution Shape ---")
        for key, val in distribution_metrics.items():
            label = "Positive" if val > 0 else ("Negative" if val < 0 else "Zero")
            metric_name = f"{key.replace('_', ' ').title()}"
            print(f"{metric_name}: {val:.4f} ({label})")
    except Exception as e:
        print(f"Error during analysis: {e}")
if __name__ == '__main__':
    main()