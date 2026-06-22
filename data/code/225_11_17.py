import numpy as np

def find_min_max(numbers: list) -> tuple:
    array = np.array(numbers)
    return (array.min(), array.max())

if __name__ == '__main__':
    sample_values = [3.14, 2.71, 1.618, 0.577, 1.414]
    min_val, max_val = find_min_max(sample_values)
    print(f"Minimum: {min_val}, Maximum: {max_val}")