import numpy as np

class DataAnalyzer:
    def __init__(self, data):
        self.data = np.array(data)

    def calculate_average(self):
        return np.mean(self.data).astype(float)

if __name__ == '__main__':
    analyzer1 = DataAnalyzer([1, 2, 3, 4, 5])
    print(f"Average of [1, 2, 3, 4, 5]: {analyzer1.calculate_average()}")

    analyzer2 = DataAnalyzer([10.5, 20.5, 30.5])
    print(f"Average of [10.5, 20.5, 30.5]: {analyzer2.calculate_average()}")