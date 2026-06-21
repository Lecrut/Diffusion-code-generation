import numpy as np

def validate_data(data):
    if not data:
        raise ValueError("Input list cannot be empty")

def calculate_average(data):
    validate_data(data)
    return float(np.mean(data))

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    average = calculate_average(sample_data)
    print(average)