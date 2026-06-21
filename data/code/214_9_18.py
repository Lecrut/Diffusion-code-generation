def find_min_value(numbers):
    if not numbers:
        raise ValueError("Input list is empty")
    
    min_value = numbers[0]
    for number in numbers[1:]:
        if number < min_value:
            min_value = number
    
    return min_value

if __name__ == '__main__':
    sample_values = [12, 34, -5, 67, 89, 0]
    result = find_min_value(sample_values)
    print(result)