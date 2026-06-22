import numpy as np

def find_min_max(data: list) -> tuple:
    if not data:
        raise ValueError("Input list cannot be empty")
    return (np.min(data), np.max(data))

if __name__ == '__main__':
    sample_values = {
        'list1': [3.14, 2.71, 1.618, 0.577, 1.414],
        'list2': [-1.11, 2.22, -3.33, 4.44, -5.55]
    }
    
    for key, value in sample_values.items():
        result = find_min_max(value)
        print(f"List: {value}, Min: {result[0]}, Max: {result[1]}")