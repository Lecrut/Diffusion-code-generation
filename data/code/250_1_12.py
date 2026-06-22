import numpy as np

class AverageCalculator:
    def __init__(self, data):
        self.data = np.array(data)

    def calculate_average(self):
        return np.mean(self.data)

if __name__ == '__main__':
    calculator1 = AverageCalculator([1.0, 2.0, 3.0, 4.0, 5.0])
    print(f"Average of {calculator1.data.tolist()}: {calculator1.calculate_average()}")

    calculator2 = AverageCalculator([10.5, 20.5, 30.5])
    print(f"Average of {calculator2.data.tolist()}: {calculator2.calculate_average()}")