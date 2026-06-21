def running_min_max(iterable):
    try:
        min_val = max_val = next(iter(iterable))
        yield (min_val, max_val)
        for value in iterable:
            if value < min_val:
                min_val = value
            elif value > max_val:
                max_val = value
            yield (min_val, max_val)
    except StopIteration:
        return

if __name__ == '__main__':
    sample_data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    for min_val, max_val in running_min_max(sample_data):
        print(f"Min: {min_val}, Max: {max_val}")