def find_max_number(numbers):
    if not numbers:
        raise ValueError("Input string cannot be empty")
    
    max_value = int(numbers[0])
    for number in numbers.split():
        current_number = int(number)
        if current_number > max_value:
            max_value = current_number
    
    return max_value

if __name__ == '__main__':
    sample_string = "3 6 2 8 1"
    try:
        maximum = find_max_number(sample_string)
        print(maximum)
    except ValueError as e:
        print(e)