import numpy as np

class MaxFinder:
    def __init__(self):
        self._data = []

    def add_data(self, data):
        self._data.extend(data)

    def get_maximum(self):
        if not self._data:
            raise ValueError("The list is empty")
        return max(self._data)

if __name__ == '__main__':
    mf = MaxFinder()
    sample_data1 = [10, 5, 20, 8]
    sample_data2 = [3, 99, 42, 7]
    mf.add_data(sample_data1)
    max1 = mf.get_maximum()
    print(f"Maximum of {sample_data1}: {max1}")
    mf.add_data(sample_data2)
    max2 = mf.get_maximum()
    print(f"Maximum of combined data: {max2}")