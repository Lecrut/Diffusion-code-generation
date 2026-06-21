def find_minimum(numbers):
    if not numbers:
        raise ValueError("Input list cannot be empty")
    
    min_value = numbers[0]
    for number in numbers[1:]:
        if number < min_value:
            min_value = number
    
    return min_value

if __name__ == '__main__':
    sample_values = [12, 34, 56, 78, -10, 0]
    print(find_minimum(sample_values))