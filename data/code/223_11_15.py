def find_max_element(numbers):
    if not numbers:
        raise ValueError("The list cannot be empty.")
    
    max_element = numbers[0]
    for number in numbers:
        if number > max_element:
            max_element = number
    
    return max_element

if __name__ == '__main__':
    sample_values = [3.14, 2.718, 1.618, 0.577, 1.414]
    try:
        result = find_max_element(sample_values)
        print(result)
    except ValueError as e:
        print(e)