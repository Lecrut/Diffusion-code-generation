def find_max_element(numbers):
    if not numbers:
        raise ValueError("Input list is empty")
    
    max_element = numbers[0]
    for number in numbers:
        if isinstance(number, (int, float)) and number > max_element:
            max_element = number
    
    return max_element

if __name__ == '__main__':
    sample_values = [3.14, 2.718, 1.618, 0.577, 1.414]
    result = find_max_element(sample_values)
    print(result)