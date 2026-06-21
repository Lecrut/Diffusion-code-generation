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
    sample_data = [7, 2, 5, 3, 8, 1]
    for current_min, current_max in running_min_max(sample_data):
        print(f"Current Min: {current_min}, Current Max: {current_max}")