import numpy as np

class MaxFinder:
    MAX_VALUE = np.inf
    
    def __init__(self, data):
        self._data = data
        self._maximum = self.MAX_VALUE if not data else max(data)
    
    def get_maximum(self):
        return self._maximum

if __name__ == '__main__':
    sample_data = [3, 5, 1, 2, 4]
    finder = MaxFinder(sample_data)
    print(finder.get_maximum())