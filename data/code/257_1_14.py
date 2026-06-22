def calculate_range(numbers):
    if not numbers:
        return None
    smallest = float('inf')
    largest = float('-inf')
    for number in numbers:
        if number < smallest:
            smallest = number
        elif number > largest:
            largest = number
    return largest - smallest

if __name__ == '__main__':
    sample_values = (5.7, 2.3, 8.9, 1.4, 6.0)
    result = calculate_range(sample_values)
    print(result)