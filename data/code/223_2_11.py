def find_max(iterable):
    max_value = None
    for item in iterable:
        if max_value is None or item > max_value:
            max_value = item
    return max_value

if __name__ == '__main__':
    sample_values = [3, 5, 1, 2, 4]
    print(find_max(sample_values))