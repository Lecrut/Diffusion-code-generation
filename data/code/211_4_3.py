import scipy.stats as stats

def compare_samples(sample1, sample2):
    shapiro_wilk_test_result = stats.shapiro(sample1)
    t_test_result = stats.ttest_ind(sample1, sample2, equal_var=True)
    return shapiro_wilk_test_result, t_test_result

if __name__ == '__main__':
    sample1 = [40.0, 42.5, 43.3, 44.8, 46.7]
    sample2 = [41.2, 41.9, 42.6, 43.1, 44.0]
    
    shapiro_wilk_test_result, t_test_result = compare_samples(sample1, sample2)
    
    print("Shapiro-Wilk Test Result for Sample 1:", shapiro_wilk_test_result)
    print("Shapiro-Wilk Test Result for Sample 2:", shapiro_wilk_test_result)
    print("T-Test Result Assuming Equal Variances:", t_test_result)