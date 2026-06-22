def find_largest_element(numbers):
    if not numbers:
        raise ValueError("Input list cannot be empty")
    
    largest = numbers[0]
    for number in numbers:
        if not isinstance(number, (int, float)):
            raise TypeError("All elements must be floats or integers")
        if number > largest:
            largest = number
    return largest

if __name__ == '__main__':
    sample_values = [3.14, 2.718, 1.618, 0.577, 1.414]
    print(find_largest_element(sample_values))