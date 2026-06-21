import numpy as np
from scipy.stats import shapiro, ttest_ind

def compare_samples(sample1, sample2):
    stat1, p1 = shapiro(sample1)
    stat2, p2 = shapiro(sample2)
    t_stat, p_value = ttest_ind(sample1, sample2, equal_var=True)
    return ((stat1, p1), (stat2, p2), (t_stat, p_value))
if __name__ == '__main__':
    sample1 = np.array([38.7, 41.5, 43.8, 44.5, 46.0])
    sample2 = np.array([40.0, 42.0, 43.0, 44.0, 45.0])
    normality_results, t_test_result = compare_samples(sample1, sample2)
    print('Shapiro-Wilk test results for sample1:', normality_results[0], 'p-value:', normality_results[1])
    print('Shapiro-Wilk test results for sample2:', normality_results[1], 'p-value:', normality_results[1])
    print('T-test result:', t_test_result)