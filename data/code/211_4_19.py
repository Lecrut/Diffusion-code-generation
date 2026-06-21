from scipy.stats import shapiro, ttest_ind

def compare_samples(sample1, sample2):
    sw1 = shapiro(sample1)
    sw2 = shapiro(sample2)
    
    print(f"Shapiro-Wilk test for sample 1: statistic={sw1.statistic}, p-value={sw1.pvalue}")
    print(f"Shapiro-Wilk test for sample 2: statistic={sw2.statistic}, p-value={sw2.pvalue}")
    
    t_stat, p_value = ttest_ind(sample1, sample2)
    print(f"T-test assuming equal variances: statistic={t_stat}, p-value={p_value}")

if __name__ == '__main__':
    sample1 = [38.7, 41.5, 43.8, 44.5, 46.0]
    sample2 = [39.0, 39.5, 40.0, 40.5, 41.0]
    
    compare_samples(sample1, sample2)