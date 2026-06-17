import math
def find_min_max(data):
    if not data:
        return None, None
    minimum = data[0]
    maximum = data[0]
    for element in data[1:]:
        if element < minimum:
            minimum = element
        if element > maximum:
            maximum = element
    return minimum, maximum
if __name__ == '__main__':
    large_list = [3.14159, -0.5, 100.7, -99.999, 55.2, 0.001, 12345.6789]
    min_val, max_val = find_min_max(large_list)
    print(f"The list is: {large_list}")
    print(f"Minimum element: {min_val}")
    print(f"Maximum element: {max_val}")