import numpy as np

def calculate_average(data):
    if not data.size > 0:
        raise ValueError("Input array cannot be empty")
    return np.mean(data)

if __name__ == '__main__':
    arr1 = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
    arr2 = np.array([10.5, 20.5, 30.5])
    empty_arr = np.array([])
    
    try:
        avg1 = calculate_average(arr1)
        print(f"Average of {arr1}: {avg1}")
        avg2 = calculate_average(arr2)
        print(f"Average of {arr2}: {avg2}")
        calculate_average(empty_arr)
    except ValueError as e:
        print(f"Error caught: {e}")