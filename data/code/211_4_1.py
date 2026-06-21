import scipy.stats as stats

def compare_samples(sample1, sample2):
    shapiro_wilk_test_result = stats.shapiro(sample1)
    t_test_result = stats.ttest_ind(sample1, sample2, equal_var=True)
    
    return shapiro_wilk_test_result, t_test_result

if __name__ == '__main__':
    sample1 = [38.7, 41.5, 43.8, 44.5, 46.0]
    sample2 = [39.0, 39.5, 40.0, 40.5, 41.0]
    
    shapiro_wilk_test_result, t_test_result = compare_samples(sample1, sample2)
    
    print("Shapiro-Wilk Test Result:", shapiro_wilk_test_result)
    print("T-Test Result:", t_test_result)