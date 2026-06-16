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
            self.data_a = arr_a.astype(np.float64)
            self.data_b = arr_b.astype(np.float64)
        except Exception as e:
            raise RuntimeError(f"Failed to load data due to {e}")
    def compute_mean(self, dataset):
        return float(np.mean(dataset))
    def compute_variance(self, dataset):
        return float(np.var(dataset, ddof=0))
    def compute_std_deviation(self, dataset):
        var = self.compute_variance(dataset)
        return np.sqrt(var)
    def perform_t_test(self):
        n_a = len(self.data_a)
        n_b = len(self.data_b)
        mean_a = self.compute_mean(self.data_a)
        mean_b = self.compute_mean(self.data_b)
        var_pooled = ((n_a - 1) * np.var(self.data_a, ddof=0) + (n_b - 1) * np.var(self.data_b, ddof=0)) / (n_a + n_b - 2)
        se = np.sqrt(var_pooled * (1/n_a + 1/n_b))
        if se == 0:
            return {'t_statistic': float('inf'), 'p_value': 0.0, 'degrees_of_freedom': n_a + n_b - 2}
        t_val = abs(mean_a - mean_b) / se
        try:
            from scipy import stats as sp_stats
            df = n_a + n_b - 2
            two_tail_p = sp_stats.t.sf(t_val, df=df) * 2.0
            return {
                't_statistic': float(t_val), 
                'p_value': float(two_tail_p), 
                'degrees_of_freedom': int(df)
            }
        except ImportError:
            import math
            df = n_a + n_b - 2
            t_val_abs = abs(mean_a - mean_b) / se
            if t_val == 0.0 or np.isinf(t_val):
                return {'t_statistic': float('nan'), 'p_value': 1.0, 'degrees_of_freedom': int(df)}
            z_approx = t_val_abs / math.sqrt(2 * (df + 2)) 
            p_norm = 2 * (1 - self._approx_cdf(z_approx))
            return {
                't_statistic': float(t_val),
                'p_value': min(float(p_norm), 0.95),                                                 
                'degrees_of_freedom': int(df)
            }
    def _approx_cdf(self, x):
        return 0.5 * (1 + np.erf(x / math.sqrt(2)))
def main():
    dataset_a = [34, 67, 89, 12, 45, 78, 90, 11, 56, 33] * 1000
    dataset_b = [40, 65, 85, 15, 50, 75, 88, 20, 60, 35] * 1000
    comparator = DistributionComparator()
    try:
        comparator.load_data(dataset_a, dataset_b)
        stats_a = {
            'mean': comparator.compute_mean(comparator.data_a),
            'std_dev': comparator.compute_std_deviation(comparator.data_a),
            'variance': comparator.compute_variance(comparator.data_a)
        }
        stats_b = {
            'mean': comparator.compute_mean(comparator.data_b),
            'std_dev': comparator.compute_std_deviation(comparator.data_b),
            'variance': comparator.compute_variance(comparator.data_b)
        }
        t_test_result = comparator.perform_t_test()
        print("=== Statistical Distribution Comparison ===")
        print(f"Dataset A: Mean={stats_a['mean']:.2f}, Std Dev={stats_a['std_dev']:.2f}")
        print(f"Dataset B: Mean={stats_b['mean']:.2f}, Std Dev={stats_b['std_dev']:.2f}")
        if 't_statistic' in t_test_result and not np.isnan(t_test_result.get('t_statistic', 0)):
            print("\nT-Test Results:")
            print(f"T-statistic: {t_test_result['t_statistic']:.4f}")
            print(f"P-value (2-tailed): {t_test_result['p_value']:.6e}")
            print(f"Degrees of Freedom: {t_test_result['degrees_of_freedom']}")
        else:
            print("\nT-Test Results:")
            print("Could not compute valid t-statistic.")
    except Exception as e:
        print(f"Error during analysis: {e}")
if __name__ == '__main__':
    main()