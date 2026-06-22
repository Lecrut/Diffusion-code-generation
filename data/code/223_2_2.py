def find_max(iterable):
    max_value = None
    for value in iterable:
        if max_value is None or value > max_value:
            max_value = value
    return max_value

if __name__ == '__main__':
    sample_values = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print(find_max(sample_values))