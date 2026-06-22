import numpy as np

class MaxFinder:
    @staticmethod
    def find_max_value(data):
        return np.max(data)

if __name__ == '__main__':
    sample_data = [3, 5, 1, 2, 4]
    max_finder = MaxFinder()
    print(max_finder.find_max_value(sample_data))