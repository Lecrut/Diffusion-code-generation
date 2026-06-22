def find_min_max(iterable):
    min_val = max_val = next(iter(iterable))
    for element in iterable:
        if element < min_val:
            min_val = element
        elif element > max_val:
            max_val = element
    return min_val, max_val

if __name__ == '__main__':
    sample_values = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print(find_min_max(sample_values))