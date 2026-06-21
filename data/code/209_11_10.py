import numpy as np

def calculate_average(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    return np.mean(data).astype(float)

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    try:
        avg = calculate_average(sample_data)
        print(f"Average of {sample_data}: {avg}")
    except ValueError as e:
        print(f"Error: {e}")