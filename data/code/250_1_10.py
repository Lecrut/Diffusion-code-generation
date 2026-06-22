import numpy as np

def calculate_average(data):
    if not data:
        raise ValueError("Input array cannot be empty")
    return np.mean(data)

if __name__ == '__main__':
    sample_array = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
    try:
        avg = calculate_average(sample_array)
        print(f"Average of {sample_array}: {avg}")
    except ValueError as e:
        print(f"Error caught: {e}")