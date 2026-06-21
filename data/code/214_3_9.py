def find_smallest_element(tup):
    if not isinstance(tup, tuple) or not all(isinstance(x, int) for x in tup):
        raise ValueError("Input must be a tuple of integers")
    if len(tup) == 0:
        raise ValueError("Tuple cannot be empty")
    return min(tup)

if __name__ == '__main__':
    sample_tuple = (5, 3, 9, 1, 4)
    print(find_smallest_element(sample_tuple))