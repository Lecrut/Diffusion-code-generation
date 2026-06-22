import numpy as np

class MaxFinder:
    MAX_VALUE = float('-inf')

    def __init__(self, data):
        self._data = data
        self._maximum = None
        self._setup()

    def _setup(self):
        if not self._data:
            self._maximum = None
            return
        self._maximum = MaxFinder.MAX_VALUE
        for item in self._data:
            if item > self._maximum:
                self._maximum = item

    def get_maximum(self):
        if self._maximum is None:
            raise ValueError("The list is empty")
        return self._maximum

if __name__ == '__main__':
    sample_data = np.array([10, 20, 30, 40, 50])
    finder = MaxFinder(sample_data)
    print(finder.get_maximum())