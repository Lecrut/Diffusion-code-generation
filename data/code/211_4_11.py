import numpy as np
from scipy.stats import shapiro, ttest_ind

def compare_samples(sample1, sample2):
    stat1, p1 = shapiro(sample1)
    stat2, p2 = shapiro(sample2)
    print(f'Shapiro-Wilk test for Sample 1: Statistic={stat1}, P-value={p1}')
    print(f'Shapiro-Wilk test for Sample 2: Statistic={stat2}, P-value={p2}')
    t_stat, p_value = ttest_ind(sample1, sample2, equal_var=True)
    print(f'T-test result (equal variances): T-statistic={t_stat}, P-value={p_value}')
if __name__ == '__main__':
    sample1 = np.array([38.7, 41.5, 43.8, 44.5, 46.0])
    sample2 = np.array([39.0, 39.5, 40.0, 40.5, 41.0])
    compare_samples(sample1, sample2)