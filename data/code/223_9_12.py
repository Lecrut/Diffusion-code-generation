import numpy as np

class MaxFinder:
    @staticmethod
    def find_max_value(data):
        return np.max(data)

if __name__ == '__main__':
    sample_data = [10, 5, 20, 8, 15]
    max_finder = MaxFinder()
    largest = max_finder.find_max_value(sample_data)
    print(largest)