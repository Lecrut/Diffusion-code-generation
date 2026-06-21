import numpy as np

class DataRangeCalculator:
    def __init__(self, data):
        self.data = np.array(data)

    def calculate_range(self):
        if not self.data.size:
            return 0.0
        return np.max(self.data) - np.min(self.data)

if __name__ == '__main__':
    calculator1 = DataRangeCalculator([1.5, 3.2, 0.9, 5.8, 2.1])
    print(f"Data: [1.5, 3.2, 0.9, 5.8, 2.1], Range: {calculator1.calculate_range()}")
    
    calculator2 = DataRangeCalculator([10.0, 5.0, 20.0, 1.0])
    print(f"Data: [10.0, 5.0, 20.0, 1.0], Range: {calculator2.calculate_range()}")
    
    calculator3 = DataRangeCalculator([7.7, 7.7, 7.7])
    print(f"Data: [7.7, 7.7, 7.7], Range: {calculator3.calculate_range()}")
    
    calculator4 = DataRangeCalculator([])
    print(f"Data: [], Range: {calculator4.calculate_range()}")