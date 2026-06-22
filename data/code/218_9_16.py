import numpy as np

class MinFinder:
    def __init__(self, data):
        self.data = data

    def find_minimum(self):
        if not self.data.size:
            raise ValueError("Input array cannot be empty")
        return np.amin(self.data)

if __name__ == '__main__':
    sample_array_1 = np.array([3, 1, 4, 1, 5, 9, 2])
    sample_array_2 = np.array([-10, 5, 0, -20, 15])
    sample_array_3 = np.array([7])

    min_finder_1 = MinFinder(sample_array_1)
    print(f"Array: {sample_array_1}")