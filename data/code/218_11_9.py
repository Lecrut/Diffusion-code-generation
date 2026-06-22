def find_smallest_element(tup):
    if not tup:
        raise ValueError("Tuple is empty")
    smallest = tup[0]
    for element in tup:
        if element < smallest:
            smallest = element
    return smallest

if __name__ == '__main__':
    sample_tuple = (5, 3, 9, 1, 7)
    print(find_smallest_element(sample_tuple))