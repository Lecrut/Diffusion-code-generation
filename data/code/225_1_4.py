def find_min_max(iterable):
    min_val = max_val = iterable[0]
    for item in iterable:
        if item < min_val:
            min_val = item
        elif item > max_val:
            max_val = item
    return min_val, max_val

if __name__ == '__main__':
    sample_values = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print(find_min_max(sample_values))