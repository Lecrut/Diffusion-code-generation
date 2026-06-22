import numpy as np

def calculate_average(data):
    if not isinstance(data, (list, np.ndarray)) or len(data) == 0:
        raise ValueError("Input must be a non-empty list or NumPy array")
    return np.mean(data)

if __name__ == '__main__':
    list1 = [1.0, 2.0, 3.0, 4.0, 5.0]
    array1 = np.array([10.5, 20.5, 30.5])
    empty_list = []
    
    try:
        avg_list1 = calculate_average(list1)
        print(f"Average of {list1}: {avg_list1}")
        
        avg_array1 = calculate_average(array1)
        print(f"Average of {array1}: {avg_array1}")
        
        calculate_average(empty_list)
    except ValueError as e:
        print(f"Error caught: {e}")