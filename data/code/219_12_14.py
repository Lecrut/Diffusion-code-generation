import numpy as np

MAX_VAL = np.inf

class MaxFinder:
    def __init__(self, data):
        self._data = data
        self._maximum = None if not data else data[0]
    
    def find_max(self):
        for item in self._data[1:]:
            if item > self._maximum:
                self._maximum = item
        return self._maximum

if __name__ == '__main__':
    sample_array = np.array([3, 5, 1, 2, 4])
    max_finder = MaxFinder(sample_array)
    print(max_finder.find_max())