import numpy as np

def validate_values(values):
    if not all(isinstance(x, (int, float)) for x in values):
        raise ValueError("All elements in the input list must be integers or floats.")

def calculate_average(values):
    return np.mean(values)

if __name__ == '__main__':
    sample_values = [100, 200, 300]
    validate_values(sample_values)
    average = calculate_average(sample_values)
    print(average)