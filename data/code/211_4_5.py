import scipy.stats as stats

class SampleComparer:
    def __init__(self, sample1, sample2):
        self.sample1 = sample1
        self.sample2 = sample2
    
    def compare_normality(self):
        shapiro_wilk_test_result = stats.shapiro(self.sample1)
        return shapiro_wilk_test_result
    
    def perform_ttest(self):
        t_test_result = stats.ttest_ind(self.sample1, self.sample2, equal_var=True)
        return t_test_result

if __name__ == '__main__':
    comparer = SampleComparer([38.7, 41.5, 43.8, 44.5, 46.0], [39.0, 39.5, 40.0, 40.5, 41.0])
    shapiro_wilk_test_result = comparer.compare_normality()
    t_test_result = comparer.perform_ttest()
    
    print("Shapiro-Wilk Test Result for Sample 1:", shapiro_wilk_test_result)
    print("T-Test Result Assuming Equal Variances:", t_test_result)