def find_smallest_value(numbers):
    if not numbers:
        return None
    smallest = float('inf')
    for number in numbers:
        if number < smallest:
            smallest = number
    return smallest

if __name__ == '__main__':
    sample_values = [8, 3, 10, 2, 5, 7]
    print(find_smallest_value(sample_values))