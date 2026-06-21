import numpy as np

class ArrayAnalyzer:
    def __init__(self, arr):
        self.arr = np.array(arr)
    
    def find_middle_value(self):
        sorted_arr = np.sort(self.arr)
        length = len(sorted_arr)
        if length % 2 == 0:
            return (sorted_arr[length // 2 - 1] + sorted_arr[length // 2]) / 2
        else:
            return sorted_arr[length // 2]

if __name__ == '__main__':
    sample_values = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    analyzer = ArrayAnalyzer(sample_values)
    print(analyzer.find_middle_value())