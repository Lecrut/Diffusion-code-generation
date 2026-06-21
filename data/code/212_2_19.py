import numpy as np

class MinMaxCalculator:
    def __init__(self):
        self.data = None
    
    def set_data(self, data):
        if not isinstance(data, np.ndarray):
            raise ValueError("Data must be a numpy array")
        self.data = data
    
    def find_min_max(self):
        if self.data is None or len(self.data) == 0:
            return None, None
        
        minimum = np.min(self.data)
        maximum = np.max(self.data)
        
        return minimum, maximum

if __name__ == '__main__':
    sample_array = np.array([15, 3, 8, 22, 1, 40])
    calculator = MinMaxCalculator()
    calculator.set_data(sample_array)
    min_val, max_val = calculator.find_min_max()
    print(f"Array: {sample_array}")
    print(f"Minimum value: {min_val}")
    print(f"Maximum value: {max_val}")