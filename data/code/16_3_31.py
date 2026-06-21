def check_all_positive(numbers):
    if not isinstance(numbers, list):
        raise ValueError("Input must be a list")
    
    for number in numbers:
        if not isinstance(number, (int, float)):
            raise ValueError("All elements in the list must be numbers")
        if number <= 0:
            return False
    return True

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5]
    try:
        print(check_all_positive(sample_values))
    except ValueError as e:
        print(e)

    invalid_sample_values = [1, 'a', 3, 4, 5]
    try:
        print(check_all_positive(invalid_sample_values))
    except ValueError as e:
        print(e)