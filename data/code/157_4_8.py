def find_smallest_value(numbers):
    if not all(isinstance(n, (int, float)) for n in numbers):
        raise ValueError("All elements in the list must be numeric")
    smallest = None
    for number in numbers:
        if smallest is None or number < smallest:
            smallest = number
    return smallest

if __name__ == '__main__':
    sample_values = [5, -2, 3, -8, 0]
    print(find_smallest_value(sample_values))