def find_min_max(data):
    if not data:
        return
    minimum = data[0]
    maximum = data[0]
    for item in data[1:]:
        if item < minimum:
            minimum = item
        if item > maximum:
            maximum = item
    yield minimum
    yield maximum
if __name__ == '__main__':
    large_list = [3.14159, 1.0, 99.9, -5.5, 42, 1000000, -123456789]
    min_val = None
    max_val = None
    for val in find_min_max(large_list):
        if min_val is None:
            min_val = val
        elif max_val is None:
            max_val = val
        else:
            pass
    print(f"Minimum: {min_val}")
    print(f"Maximum: {max_val}")
    empty_list = []
    for val in find_min_max(empty_list):
        pass
    print("Empty list test complete")