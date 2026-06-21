import scipy.stats as stats

def compare_samples(sample1, sample2):
    shapiro_wilk_test = stats.shapiro(sample1)
    t_test = stats.ttest_ind(sample1, sample2, equal_var=True)
    return shapiro_wilk_test, t_test

if __name__ == '__main__':
    sample1 = [38.7, 41.5, 43.8, 44.5, 46.0]
    sample2 = [39.0, 39.5, 40.0, 40.5, 41.0]
    shapiro_wilk_test, t_test = compare_samples(sample1, sample2)
    print("Shapiro-Wilk Test:", shapiro_wilk_test)
    print("T-Test (Equal Variances):", t_test)