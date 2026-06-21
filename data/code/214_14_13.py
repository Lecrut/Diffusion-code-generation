def find_minimum_value(numbers):
    if not numbers:
        raise ValueError("The input list cannot be empty")
    
    min_value = numbers[0]
    for number in numbers[1:]:
        if number < min_value:
            min_value = number
    
    return min_value

if __name__ == '__main__':
    sample_data = [7, 3, 5, 2, 9, 1]
    try:
        smallest_number = find_minimum_value(sample_data)
        print(smallest_number)
    except ValueError as e:
        print(e)