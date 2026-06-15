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
    sample_list = [3.14159, -0.5, 100.75, -12.345, 55.0, 0.0]
    min_val, max_val = find_min_max(sample_list)
    print(f"The list is: {sample_list}")
    print(f"Minimum element: {min_val}")
    print(f"Maximum element: {max_val}")