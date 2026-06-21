import scipy.stats as stats

def compare_samples(sample1, sample2):
    shapiro_wilk_test_sample1 = stats.shapiro(sample1)
    shapiro_wilk_test_sample2 = stats.shapiro(sample2)

    t_test_result = stats.ttest_ind(sample1, sample2, equal_var=True)

    return shapiro_wilk_test_sample1, shapiro_wilk_test_sample2, t_test_result

if __name__ == '__main__':
    sample1 = [38.7, 41.5, 43.8, 44.5, 46.0]
    sample2 = [39.0, 39.5, 40.0, 40.5, 41.0]

    sw_test_sample1, sw_test_sample2, t_test_result = compare_samples(sample1, sample2)

    print("Shapiro-Wilk test for sample1:", sw_test_sample1)
    print("Shapiro-Wilk test for sample2:", sw_test_sample2)
    print("T-test result (assuming equal variances):", t_test_result)