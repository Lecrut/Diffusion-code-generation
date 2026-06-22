import numpy as np

def find_min_max(values: list) -> tuple:
    arr = np.array(values)
    return np.min(arr), np.max(arr)

if __name__ == '__main__':
    sample_values = [3.14, 2.71, 1.618, 0.577, 1.414]
    min_val, max_val = find_min_max(sample_values)
    print(f"Minimum: {min_val}, Maximum: {max_val}")