import math
def find_min_max(data):
    if not data:
        return None, None
    minimum = data[0]
    maximum = data[0]
    for element in data:
        if element < minimum:
            minimum = element
        if element > maximum:
            maximum = element
    return minimum, maximum
if __name__ == '__main__':
    sample_list = [3.14159, -0.5, 100.75, -12.3, 55.0, 0.0, 999.99]
    min_val, max_val = find_min_max(sample_list)
    print(f"Sample List: {sample_list}")
    print(f"Minimum element: {min_val}")
    print(f"Maximum element: {max_val}")