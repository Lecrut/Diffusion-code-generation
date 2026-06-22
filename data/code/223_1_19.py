def find_largest_element(numbers):
    if not all(isinstance(num, float) for num in numbers):
        raise ValueError("All elements must be floats")
    
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest

if __name__ == '__main__':
    sample_values = [3.14, 2.718, 1.618, 0.577, 1.414]
    print(find_largest_element(sample_values))