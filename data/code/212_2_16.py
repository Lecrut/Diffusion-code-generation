import numpy as np

class MinMaxCalculator:
    def calculate_min_max(self, data):
        if not isinstance(data, np.ndarray) or data.size == 0:
            raise ValueError("Input must be a non-empty numpy array")
        
        minimum = np.min(data)
        maximum = np.max(data)
        
        return minimum, maximum

if __name__ == '__main__':
    calculator = MinMaxCalculator()
    sample_array = np.array([15, 3, 8, 22, 1, 40])
    try:
        minimum_val, maximum_val = calculator.calculate_min_max(sample_array)
        print(f"Array: {sample_array}")
        print(f"Minimum value: {minimum_val}")
        print(f"Maximum value: {maximum_val}")
    except ValueError as e:
        print(e)