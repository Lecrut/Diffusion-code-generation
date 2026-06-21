import numpy as np

class MedianFinder:
    _arr = None
    
    def __init__(self, arr):
        self._arr = np.array(arr)
    
    @staticmethod
    def sort_and_find_mid(arr):
        sorted_arr = np.sort(arr)
        length = len(sorted_arr)
        if length % 2 == 0:
            return (sorted_arr[length // 2 - 1] + sorted_arr[length // 2]) / 2
        else:
            return sorted_arr[length // 2]
    
    def find_middle_value(self):
        return self.sort_and_find_mid(self._arr)

if __name__ == '__main__':
    sample_values = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    finder = MedianFinder(sample_values)
    print(finder.find_middle_value())