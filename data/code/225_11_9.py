import numpy as np

def find_min_max(data: list) -> tuple:
    if not data:
        raise ValueError("Input list cannot be empty")
    
    arr = np.array(data)
    minimum = np.min(arr)
    maximum = np.max(arr)
    
    return (minimum, maximum)

if __name__ == '__main__':
    sample_data1 = [3.14, 2.71, 1.618, 0.577, 1.414]
    result1 = find_min_max(sample_data1)
    print(f"List: {sample_data1}, Min: {result1[0]}, Max: {result1[1]}")
    
    sample_data2 = [100.0, -50.0, 25.0, 75.0]
    result2 = find_min_max(sample_data2)
    print(f"List: {sample_data2}, Min: {result2[0]}, Max: {result2[1]}")