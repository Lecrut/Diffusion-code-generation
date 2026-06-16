import numpy as np
class DistributionComparator:
    def __init__(self):
        self.data_a = None
        self.data_b = None
    def load_data(self, data_list_a, data_list_b):
        try:
            arr_a = np.array(data_list_a)
            arr_b = np.array(data_list_b)
            if len(arr_a) == 0 or len(arr_b) == 0:
                raise ValueError("Datasets cannot be empty.")
            self.data_a = arr_a
            self.data_b = arr_b
        except Exception as e:
            print(f"Error loading data: {e}")
    def compute_mean(self, array):
        return float(np.mean(array))
    def compute_variance(self, array):
        return float(np.var(array))
    def compute_std_deviation(self, array):
        return self.compute_variance(array) ** 0.5
    def compute_skewness(self, array):
        mean = np.mean(array)
        std_dev = np.std(array, ddof=1) if len(array) > 1 else 0
        if std_dev == 0:
            return 0.0
        numerator = np.sum(((array - mean) ** 3)) / (len(array) * std_dev**3)
        n = len(array)
        bias_correction_factor = ((n + 1) * n) / (((n - 1) * (n - 2))) if n > 2 else 0
        return float(numerator * bias_correction_factor)
    def compute_kurtosis(self, array):
        mean = np.mean(array)
        std_dev = np.std(array, ddof=1) if len(array) > 0 else 0
        if std_dev == 0:
            return 0.0
        numerator = np.sum(((array - mean) ** 4)) / (len(array) * std_dev**4)
        n = len(array)
        bias_correction_factor = ((n + 1) * n * (n - 1)) / (((n - 2) * (n - 3))) if n > 3 else 0
        return float(numerator * bias_correction_factor)
    def compute_correlation(self, array_a, array_b):
        mean_a = np.mean(array_a)
        mean_b = np.mean(array_b)
        numerator = np.sum(((array_a - mean_a) * (array_b - mean_b))) / len(array_a)
        denominator_product = self.compute_std_deviation(array_a) * self.compute_std_deviation(array_b)
        if denominator_product == 0:
            return 0.0
        return float(numerator / denominator_product)
    def compare_distributions(self):
        stats = {
            'mean_a': self.compute_mean(self.data_a),
            'variance_a': self.compute_variance(self.data_a),
            'std_deviation_a': self.compute_std_deviation(self.data_a),
            'skewness_a': self.compute_skewness(self.data_a),
            'kurtosis_a': self.compute_kurtosis(self.data_a),
            'mean_b': self.compute_mean(self.data_b),
            'variance_b': self.compute_variance(self.data_b),
            'std_deviation_b': self.compute_std_deviation(self.data_b),
            'skewness_b': self.compute_skewness(self.data_b),
            'kurtosis_b': self.compute_kurtosis(self.data_b),
            'correlation_coefficient': self.compute_correlation(self.data_a, self.data_b)
        }
        return stats
if __name__ == '__main__':
    dataset_1 = [2.5, 3.0, 4.5, 5.0, 6.0, 7.5, 8.0]
    dataset_2 = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0]
    comparator = DistributionComparator()
    comparator.load_data(dataset_1, dataset_2)
    results = comparator.compare_distributions()
    print("Distribution Comparison Results")
    print("-" * 30)
    print(f"\nDataset A Statistics:")
    print(f"Mean: {results['mean_a']:.4f}")
    print(f"Variance: {results['variance_a']:.4f}")
    print(f"Standard Deviation: {results['std_deviation_a']:.4f}")
    print(f"Skewness: {results['skewness_a']:.4f}")
    print(f"Pearson Kurtosis: {results['kurtosis_a']:.4f}")
    print("\nDataset B Statistics:")
    print(f"Mean: {results['mean_b']:.4f}")
    print(f"Variance: {results['variance_b']:.4f}")
    print(f"Standard Deviation: {results['std_deviation_b']:.4f}")
    print(f"Skewness: {results['skewness_b']:.4f}")
    print(f"Pearson Kurtosis: {results['kurtosis_b']:.4f}")
    print("\nRelationship Metrics:")
    print(f"Covariance (implied via correlation): N/A")
    print(f"Correlation Coefficient: {results['correlation_coefficient']:.4f}")