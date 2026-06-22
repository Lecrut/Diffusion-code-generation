import numpy as np

class MaxFinder:
    def __init__(self):
        self._data = np.array([])
    
    def add_data(self, data):
        if not isinstance(data, np.ndarray):
            data = np.array(data)
        self._data = np.concatenate((self._data, data))
    
    def get_maximum(self):
        if len(self._data) == 0:
            raise ValueError("The array is empty")
        return np.max(self._data)

if __name__ == '__main__':
    mf = MaxFinder()
    sample_data1 = [10, 5, 20, 8]
    sample_data2 = [3, 99, 1, 42]
    mf.add_data(sample_data1)
    print(f"Maximum of {sample_data1}: {mf.get_maximum()}")
    mf.add_data(sample_data2)
    print(f"Maximum of {sample_data2}: {mf.get_maximum()}")