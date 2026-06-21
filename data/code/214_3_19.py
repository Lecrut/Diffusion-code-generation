def find_smallest_element(tup):
    if not isinstance(tup, tuple) or not all(isinstance(x, int) for x in tup):
        raise ValueError("Input must be a non-empty tuple of integers")
    return min(tup)

if __name__ == '__main__':
    sample_tuple = (5, 3, 9, 1, 7)
    print(find_smallest_element(sample_tuple))