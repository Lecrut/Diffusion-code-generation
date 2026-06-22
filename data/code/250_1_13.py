import numpy as np

def calculate_average(data):
    if not isinstance(data, np.ndarray) or data.size == 0:
        raise ValueError("Input must be a non-empty NumPy array")
    return np.mean(data)

if __name__ == '__main__':
    array1 = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
    array2 = np.array([10.5, 20.5, 30.5])
    empty_array = np.array([])
    try:
        avg1 = calculate_average(array1)
        print(f"Average of {array1}: {avg1}")
        avg2 = calculate_average(array2)
        print(f"Average of {array2}: {avg2}")
        calculate_average(empty_array)
    except ValueError as e:
        print(f"Error caught: {e}")