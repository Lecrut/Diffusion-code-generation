import numpy as np

class ArrayComparator:
    def __init__(self, arr):
        self.arr = np.array(arr)

    def compare_adjacent_elements(self):
        return np.maximum(self.arr[:-1], self.arr[1:])

if __name__ == '__main__':
    comparator_1 = ArrayComparator([1, 3, 2, 5, 4])
    result_1 = comparator_1.compare_adjacent_elements()
    print(result_1)
    
    comparator_2 = ArrayComparator([10, 8, 6, 4, 2])
    result_2 = comparator_2.compare_adjacent_elements()
    print(result_2)
    
    comparator_3 = ArrayComparator([5, 5, 5, 5])
    result_3 = comparator_3.compare_adjacent_elements()
    print(result_3)