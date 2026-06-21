def find_smallest_value(numbers):
    if not all(isinstance(n, int) for n in numbers):
        raise ValueError("All elements in the list must be integers")
    smallest = float('inf')
    for number in numbers:
        if number < smallest:
            smallest = number
    return smallest

if __name__ == '__main__':
    sample_values = [-5, 3, -1, 2, -4]
    print(find_smallest_value(sample_values))