import numpy as np

def calculate_middle_value(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    
    return np.median(data)

if __name__ == '__main__':
    sample1 = [1, 5, 2, 8, 3]
    print(calculate_middle_value(sample1))
    
    sample2 = [10, 20, 30, 40, 50, 60]
    print(calculate_middle_value(sample2))
    
    sample3 = [7]
    print(calculate_middle_value(sample3))