import numpy as np

class DataAnalyzer:
    def __init__(self, data):
        self.data = np.array(data)

    def calculate_range(self):
        return np.max(self.data) - np.min(self.data)

if __name__ == '__main__':
    analyzer1 = DataAnalyzer([1.5, 3.2, 0.9, 5.8, 2.1])
    print(f"Data: {analyzer1.data.tolist()}, Range: {analyzer1.calculate_range()}")
    
    analyzer2 = DataAnalyzer([10.0, 5.0, 20.0, 1.0])
    print(f"Data: {analyzer2.data.tolist()}, Range: {analyzer2.calculate_range()}")