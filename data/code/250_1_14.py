import numpy as np

def calculate_average(data):
    if not data.size:
        raise ValueError("Input array cannot be empty")
    return np.mean(data)

if __name__ == '__main__':
    sample_array1 = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
    sample_array2 = np.array([10.5, 20.5, 30.5])
    empty_array = np.array([])
    
    try:
        avg1 = calculate_average(sample_array1)
        print(f"Average of {sample_array1}: {avg1}")
        avg2 = calculate_average(sample_array2)
        print(f"Average of {sample_array2}: {avg2}")
        calculate_average(empty_array)
    except ValueError as e:
        print(f"Error caught: {e}")