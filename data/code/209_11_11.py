import numpy as np

class DataAnalyzer:
    def __init__(self, data):
        self.data = np.array(data)

    def calculate_average(self):
        return float(np.mean(self.data))

if __name__ == '__main__':
    analyzer1 = DataAnalyzer([1, 2, 3, 4, 5])
    print(f"Average of {analyzer1.data.tolist()}: {analyzer1.calculate_average()}")

    analyzer2 = DataAnalyzer([10.5, 20.5, 30.5])
    print(f"Average of {analyzer2.data.tolist()}: {analyzer2.calculate_average()}")