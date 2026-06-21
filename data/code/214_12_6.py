def find_smallest(iterable):
    if not iterable:
        raise ValueError("Input iterable cannot be empty")
    smallest = float('inf')
    for value in iterable:
        if not isinstance(value, (int, float)):
            raise TypeError("All elements must be numbers")
        if value < smallest:
            smallest = value
    return smallest

if __name__ == '__main__':
    sample_values = [3.14, 2.71, -1.0, 0.0, 5.0]
    print(find_smallest(sample_values))