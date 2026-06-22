def max_element(iterable):
    if not iterable:
        raise ValueError("Empty iterable")
    max_val = iterable[0]
    for element in iterable:
        if element > max_val:
            max_val = element
    return max_val

if __name__ == '__main__':
    sample_values = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print(max_element(sample_values))