import numpy as np

class DataProcessor:
    def __init__(self, data):
        self.data = np.array(data, dtype=float)

    def calculate_average(self):
        return np.mean(self.data).astype(float)

if __name__ == '__main__':
    processor1 = DataProcessor([1, 2, 3, 4, 5])
    print(f"Average of {processor1.data}: {processor1.calculate_average()}")

    processor2 = DataProcessor([10.5, 20.5, 30.5])
    print(f"Average of {processor2.data}: {processor2.calculate_average()}")