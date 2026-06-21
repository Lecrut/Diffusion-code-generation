import numpy as np

class DataComparator:
    def __init__(self, sample1, sample2):
        self.sample1 = sample1
        self.sample2 = sample2

    def compare_means(self):
        return (np.mean(self.sample1), np.mean(self.sample2))

    def compare_medians(self):
        return (np.median(self.sample1), np.median(self.sample2))

    def compare_std_devs(self):
        return (np.std(self.sample1), np.std(self.sample2))

if __name__ == '__main__':
    sample_data_set_1 = [1, 2, 3, 4, 5]
    sample_data_set_2 = [3, 4, 5, 6, 7]

    comparator = DataComparator(sample_data_set_1, sample_data_set_2)

    print(f"Means: {comparator.compare_means()}")
    print(f"Medians: {comparator.compare_medians()}")
    print(f"Standard Deviations: {comparator.compare_std_devs()}")