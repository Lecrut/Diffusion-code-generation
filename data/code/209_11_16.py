import numpy as np

def validate_data(data):
    if not isinstance(data, list) or not all(isinstance(x, (int, float)) for x in data):
        raise ValueError("Input must be a list of numbers")

def calculate_average(data):
    validate_data(data)
    return np.mean(data).astype(float)

if __name__ == '__main__':
    sample_data = [1, 2, 3, 4, 5]
    average = calculate_average(sample_data)
    print(f"Average of {sample_data}: {average}")