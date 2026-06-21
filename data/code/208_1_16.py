import numpy as np

class ArrayAnalyzer:
    def __init__(self, array):
        self.array = np.array(array, dtype=float)

    def calculate_mean(self):
        return np.mean(self.array)

if __name__ == '__main__':
    analyzer1 = ArrayAnalyzer([1, 2, 3, 4, 5])
    analyzer2 = ArrayAnalyzer([10.5, 20.5, 30.5])
    analyzer_empty = ArrayAnalyzer([])
    analyzer3 = ArrayAnalyzer([-1, 5, 10, -2])

    print(f"Mean of {analyzer1.array}: {analyzer1.calculate_mean()}")
    print(f"Mean of {analyzer2.array}: {analyzer2.calculate_mean()}")
    print(f"Mean of {analyzer_empty.array}: {analyzer_empty.calculate_mean()}")
    print(f"Mean of {analyzer3.array}: {analyzer3.calculate_mean()}")