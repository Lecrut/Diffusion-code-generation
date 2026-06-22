def find_min_max(iterable):
    min_val = max_val = next(iter(iterable))
    for value in iterable:
        if value < min_val:
            min_val = value
        elif value > max_val:
            max_val = value
    return min_val, max_val

if __name__ == '__main__':
    sample_values = (3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5)
    print(find_min_max(sample_values))