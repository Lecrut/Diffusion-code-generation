import math
def find_min_max(data):
    if not data:
        return None, None
    minimum = min(data)
    maximum = max(data)
    return minimum, maximum
if __name__ == '__main__':
    large_list = [3.141592653589793, -1.0, 100.5, 0.0, -99.999999999, 50.2]
    minimum_val, maximum_val = find_min_max(large_list)
    print(f"Minimum: {minimum_val}")
    print(f"Maximum: {maximum_val}")