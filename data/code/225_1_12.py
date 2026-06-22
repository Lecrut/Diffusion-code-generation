def find_min_max(iterable):
    min_val = max_val = iterable[0]
    for element in iterable:
        if element < min_val:
            min_val = element
        elif element > max_val:
            max_val = element
    return min_val, max_val

if __name__ == '__main__':
    sample_values = [34, 12, 98, 56, 78]
    print(find_min_max(sample_values))