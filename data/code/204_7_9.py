import numpy as np

def validate_data(data):
    if not isinstance(data, list) or not all(isinstance(x, (int, float)) for x in data):
        raise ValueError("Input must be a list of numbers")

def find_middle(data):
    validate_data(data)
    n = len(data)
    if n == 0:
        return None
    middle_index = n // 2
    return data[middle_index]

if __name__ == '__main__':
    sample1 = [1, 5, 2, 8, 3]
    print(find_middle(sample1))
    
    sample2 = [10, 20, 30, 40, 50, 60]
    print(find_middle(sample2))
    
    sample3 = [7]
    print(find_middle(sample3))
    
    sample4 = []
    print(find_middle(sample4))