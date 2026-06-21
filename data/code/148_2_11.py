def find_largest_element(numbers):
    if not numbers:
        raise ValueError("Input list is empty")
    
    largest_value = numbers[0]
    for number in numbers:
        if number > largest_value:
            largest_value = number
    
    return largest_value

if __name__ == '__main__':
    sample_data = [10, 5, 20, 15, 30]
    try:
        result = find_largest_element(sample_data)
        print(result)
    except ValueError as e:
        print(e)