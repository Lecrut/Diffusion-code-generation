import scipy.stats as stats

def perform_normality_and_ttest(sample1, sample2):
    shapiro_wilk_test = stats.shapiro(sample1)
    t_test = stats.ttest_ind(sample1, sample2, equal_var=True)
    return shapiro_wilk_test, t_test

if __name__ == '__main__':
    sample1 = [40.5, 41.3, 42.8, 43.6, 45.1]
    sample2 = [41.7, 42.2, 43.0, 43.9, 44.6]
    
    shapiro_wilk_test_result, t_test_result = perform_normality_and_ttest(sample1, sample2)
    
    print("Shapiro-Wilk Test Result for Sample 1:", shapiro_wilk_test_result)
    print("Shapiro-Wilk Test Result for Sample 2:", shapiro_wilk_test_result)
    print("T-Test Result Assuming Equal Variances:", t_test_result)