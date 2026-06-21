import numpy as np

def calculate_average(data):
    if not data:
        raise ValueError("Data list cannot be empty")
    return np.mean(data)

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    try:
        result = calculate_average(sample_data)
        print(f"Average of {sample_data}: {result}")
    except ValueError as e:
        print(e)