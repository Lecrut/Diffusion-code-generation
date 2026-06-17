import math
def find_min_max(data):
    if not data:
        return None, None
    minimum = data[0]
    maximum = data[0]
    for number in data[1:]:
        if number < minimum:
            minimum = number
        if number > maximum:
            maximum = number
    return minimum, maximum
if __name__ == '__main__':
    large_list = [3.1415926535, -10.5, 0.0, 99.999999999, -5.0, 12345.6789]
    min_val, max_val = find_min_max(large_list)
    print(f"The list is: {large_list}")
    print(f"Minimum element: {min_val}")
    print(f"Maximum element: {max_val}")