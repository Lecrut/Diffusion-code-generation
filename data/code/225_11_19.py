import numpy as np

def find_min_max(data: list) -> tuple:
    if not data:
        raise ValueError("Input list cannot be empty")
    return (np.min(data), np.max(data))

if __name__ == '__main__':
    sample_list = [3.14, 2.71, 1.618, 0.577, 1.414]
    result = find_min_max(sample_list)
    print(f"List: {sample_list}, Min: {result[0]}, Max: {result[1]}")