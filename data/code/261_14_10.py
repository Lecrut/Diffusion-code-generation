import numpy as np

def calculate_median(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    return float(np.median(data))

if __name__ == '__main__':
    list1 = [3.5, 1.2, 8.9, 4.1, 2.3]
    print(f"Median of {list1}: {calculate_median(list1)}")