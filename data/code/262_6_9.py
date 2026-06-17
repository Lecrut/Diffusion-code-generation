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
    large_list = [45, 12, 89, -3, 56, 77, 0, 99, -100, 23]
    min_val = None
    max_val = None
    generator = find_min_max(large_list)
    for result in generator:
        if min_val is None:
            min_val = result
        else:
            max_val = result
    print(f"Minimum value: {min_val}")
    print(f"Maximum value: {max_val}")
    empty_list = []
    generator_empty = find_min_max(empty_list)
    print("\nTesting empty list:")
    for _ in generator_empty:
        pass