def min_max_generator(iterable):
    if not iterable:
        return
    min_val = None
    max_val = None
    for item in iterable:
        if min_val is None:
            min_val = item
            max_val = item
        else:
            if item < min_val:
                min_val = item
            if item > max_val:
                max_val = item
        yield min_val, max_val
if __name__ == '__main__':
    sample_data = [10, 5, 20, 3, 15, 25]
    generator = min_max_generator(sample_data)
    print("Input:", sample_data)
    for current_min, current_max in generator:
        print(f"Min: {current_min}, Max: {current_max}")