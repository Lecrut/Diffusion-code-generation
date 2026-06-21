def running_min_max(iterable):
    min_val = float('inf')
    max_val = float('-inf')
    for value in iterable:
        if value < min_val:
            min_val = value
        if value > max_val:
            max_val = value
        yield (min_val, max_val)

if __name__ == '__main__':
    sample_data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    for min_val, max_val in running_min_max(sample_data):
        print(f"Min: {min_val}, Max: {max_val}")