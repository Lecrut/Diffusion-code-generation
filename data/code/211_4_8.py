from scipy.stats import shapiro, ttest_ind

def compare_samples(sample1, sample2):
    shapiro_test_sample1 = shapiro(sample1)
    shapiro_test_sample2 = shapiro(sample2)
    print('Shapiro-Wilk Test Results:')
    print(f'Sample 1: {shapiro_test_sample1}')
    print(f'Sample 2: {shapiro_test_sample2}')
    ttest_result = ttest_ind(sample1, sample2, equal_var=True)
    print('\nT-Test Result:')
    print(ttest_result)
if __name__ == '__main__':
    sample1 = [38.7, 41.5, 43.8, 44.5, 46.0]
    sample2 = [39.2, 40.1, 42.0, 43.0, 44.5]
    compare_samples(sample1, sample2)