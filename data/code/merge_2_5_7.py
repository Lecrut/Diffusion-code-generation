import numpy as np
class DistributionComparator:
    def __init__(self):
        self.data_a = None
        self.data_b = None
    def load_data(self, data_a_list, data_b_list):
        try:
            self.data_a = np.array(data_a_list)
            self.data_b = np.array(data_b_list)
            if len(self.data_a) != len(self.data_b):
                raise ValueError("Both datasets must have the same number of samples.")
        except Exception as e:
            print(f"Error loading data: {e}")
    def compute_basic_stats(self, label="data"):
        if self.data_a is not None and label == "a":
            return {"mean": float(np.mean(self.data_a)), "std": float(np.std(self.data_a))}
        elif self.data_b is not None and label == "b":
            return {"mean": float(np.mean(self.data_b)), "std": float(np.std(self.data_b))}
    def compute_correlation_matrix(self):
        if len(self.data_a) != 0:
            corr = np.corrcoef([self.data_a, self.data_b])
            return {
                "corr_ab": float(corr[0][1]),
                "covariance_matrix": [float(x) for x in list(np.array(corr).flatten())]
            }
        else:
            raise ValueError("Data is empty.")
    def compute_kurtosis(self):
        if self.data_a is not None and self.data_b is not None:
            return {
                "kurtosis_a": float(np.kurtosis(self.data_a)),
                "kurtosis_b": float(np.kurtosis(self.data_b))
            }
    def compute_skewness(self):
        if self.data_a is not None and self.data_b is not None:
            return {
                "skewness_a": float(np.skew(self.data_a)),
                "skewness_b": float(np.skew(self.data_b))
            }
def main():
    dataset_a = [10, 25, 30, 45, 60]
    dataset_b = [8, 27, 32, 48, 62]
    comparator = DistributionComparator()
    try:
        comparator.load_data(dataset_a, dataset_b)
        print("=== Basic Statistics ===")
        stats_a = comparator.compute_basic_stats(label="a")
        stats_b = comparator.compute_basic_stats(label="b")
        print(f"Dataset A - Mean: {stats_a['mean']}, Std Dev: {stats_a['std']}")
        print(f"Dataset B - Mean: {stats_b['mean']}, Std Dev: {stats_b['std']}")
        print("\n=== Skewness Analysis ===")
        skew_data = comparator.compute_skewness()
        print(f"A Skewness: {skew_data['skewness_a']}")
        print(f"B Skewness: {skew_data['skewness_b']}")
        print("\n=== Kurtosis Analysis ===")
        kurt_data = comparator.compute_kurtosis()
        print(f"A Excess Kurtosis: {kurt_data['kurtosis_a']}")
        print(f"B Excess Kurtosis: {kurt_data['kurtosis_b']}")
        print("\n=== Correlation Analysis ===")
        corr_matrix = comparator.compute_correlation_matrix()
        print(f"Correlation Coefficient (A vs B): {corr_matrix['corr_ab']:.4f}")
    except Exception as e:
        print("Error during analysis:", str(e))
if __name__ == '__main__':
    main()