import numpy as np

class MaxFinder:
    def __init__(self, data):
        self.data = np.array(data)

    def find_max(self):
        return np.max(self.data)

if __name__ == '__main__':
    sample_list = [3.14, 1.618, 2.718, 0.577, 4.0]
    finder = MaxFinder(sample_list)
    maximum = finder.find_max()
    print(f"The sample list is: {sample_list}")
    print(f"The maximum element found using vectorized operations is: {maximum}")