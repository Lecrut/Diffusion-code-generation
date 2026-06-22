def max_element(iterable):
    if not iterable:
        raise ValueError('Empty iterable')
    max_elem = iterable[0]
    for elem in iterable:
        if elem > max_elem:
            max_elem = elem
    return max_elem
if __name__ == '__main__':
    sample_values = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print(max_element(sample_values))