def find_smallest_value(numbers):
    if not numbers:
        return None
    smallest = float('inf')
    for number in numbers:
        if number < smallest:
            smallest = number
    return smallest

if __name__ == '__main__':
    sample_values = [-5, 2, 10, -8, 3, -1]
    result = find_smallest_value(sample_values)
    print(result)