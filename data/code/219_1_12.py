def max_element(iterable):
    if not iterable:
        raise ValueError('Empty iterable')
    max_elem = next(iter(iterable))
    for elem in iterable:
        if elem > max_elem:
            max_elem = elem
    return max_elem
if __name__ == '__main__':
    sample_values = [3, 5, 1, 2, 4]
    print(max_element(sample_values))