from scipy.stats import shapiro, ttest_ind

def compare_samples(sample1, sample2):
    shapiro_wilk_result = shapiro(sample1)
    print('Shapiro-Wilk Test Result:', shapiro_wilk_result)
    t_test_result = ttest_ind(sample1, sample2, equal_var=True)
    print('T-test Result:', t_test_result)
if __name__ == '__main__':
    sample1 = [38.7, 41.5, 43.8, 44.5, 46.0]
    sample2 = [39.0, 39.5, 40.0, 40.5, 41.0]
    compare_samples(sample1, sample2)