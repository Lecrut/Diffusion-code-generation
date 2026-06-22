def find_max_number(numbers):
    if not numbers:
        raise ValueError("Input string cannot be empty")
    
    try:
        number_list = list(map(float, numbers.split()))
        max_value = max(number_list)
        return max_value
    except ValueError as e:
        raise ValueError("Invalid input: All elements must be numbers") from e

if __name__ == '__main__':
    sample_string = "3.14159 2.71828 1.61803 4.0 0.5"
    try:
        maximum = find_max_number(sample_string)
        print(maximum)
    except ValueError as e:
        print(e)