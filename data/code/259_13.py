import math
def find_min_max(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    minimum = data[0]
    maximum = data[0]
    for number in data:
        if number < minimum:
            minimum = number
        if number > maximum:
            maximum = number
    return minimum, maximum
if __name__ == '__main__':
    sample_list = [3.14159, 1.61803, 2.71828, -0.57721, 100.0, -5.2]
    try:
        min_val, max_val = find_min_max(sample_list)
        print(f"The list is: {sample_list}")
        print(f"Minimum element: {min_val}")
        print(f"Maximum element: {max_val}")
    except ValueError as e:
        print(f"Error: {e}")