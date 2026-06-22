def max_generator(*args):
    max_val = None
    for val in args:
        if max_val is None or val > max_val:
            max_val = val
    return max_val

def get_largest_from_sequence(iterable):
    result = None
    for item in iterable:
        if result is None or item > result:
            result = item
    return result
if __name__ == '__main__':
    data = [15, 3, 99, 42, 7, 128, 55]
    largest_value = get_largest_from_sequence(data)
    print(largest_value)