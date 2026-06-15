import numpy as np
def find_average(data):
    if not data:
        raise ValueError("Input data cannot be empty.")
    return sum(data) / len(data)
if __name__ == '__main__':
    set1 = [1, 2, 3, 4, 5]
    set2 = [10, 20, 30]
    set3 = [2.5, 3.5, 4.5]
    set4 = [100, 50, 75, 25]
    empty_set = []
    print(f"Average of {set1}: {find_average(set1)}")
    print(f"Average of {set2}: {find_average(set2)}")
    print(f"Average of {set3}: {find_average(set3)}")
    print(f"Average of {set4}: {find_average(set4)}")
    try:
        find_average(empty_set)
    except ValueError as e:
        print(f"Error for empty set: {e}")