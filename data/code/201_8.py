import numpy as np
def calculate_average(data):
    if not data:
        raise ValueError("Input data cannot be empty.")
    try:
        average = sum(data) / len(data)
        return average
    except TypeError:
        raise TypeError("All elements in the input data must be numeric.")
if __name__ == '__main__':
    set1 = [1, 2, 3, 4, 5]
    set2 = [10.5, 20.5, 30.5]
    set3 = [-1, 0, 1, 2, -2]
    set4 = [100, 200, 300]
    empty_set = []
    mixed_set = [1, 2, 'a']
    print(f"Average of {set1}: {calculate_average(set1)}")
    print(f"Average of {set2}: {calculate_average(set2)}")
    print(f"Average of {set3}: {calculate_average(set3)}")
    print(f"Average of {set4}: {calculate_average(set4)}")
    try:
        calculate_average(empty_set)
    except ValueError as e:
        print(f"Error for empty set: {e}")
    try:
        calculate_average(mixed_set)
    except TypeError as e:
        print(f"Error for mixed set: {e}")