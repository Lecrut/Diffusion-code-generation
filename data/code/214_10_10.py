def find_minimum(numbers):
    if not numbers:
        raise ValueError("Input list cannot be empty")
    
    smallest = numbers[0]
    for number in numbers:
        if number < smallest:
            smallest = number
    
    return smallest

if __name__ == '__main__':
    sample_values = [1, 3, -5, 7, 0, 2]
    result = find_minimum(sample_values)
    print(result)