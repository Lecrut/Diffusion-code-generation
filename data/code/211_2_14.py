import numpy as np

class ArrayComparator:
    def __init__(self, array1, array2):
        self.array1 = np.array(array1)
        self.array2 = np.array(array2)

    def compute_absolute_difference(self):
        return np.abs(self.array1 - self.array2)

    def compute_sum_of_squared_errors(self):
        return np.sum((self.array1 - self.array2) ** 2)

if __name__ == '__main__':
    comparator = ArrayComparator([1, 2, 3, 4, 5], [4, 5, 6, 7, 8])
    abs_diff = comparator.compute_absolute_difference()
    sum_squared_errors = comparator.compute_sum_of_squared_errors()
    print("Absolute Difference Matrix:")
    print(abs_diff)
    print("Sum of Squared Errors:")
    print(sum_squared_errors)