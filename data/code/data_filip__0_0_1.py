def extract_digits(string):
    digits = []
    for char in string:
        if char.isdigit():
            digits.append(char)
    
    if not digits:
        return None
    
    number_str = "".join(digits)
    return int(number_str)

if __name__ == '__main__':
    test_string = "abc123def456"
    result = extract_digits(test_string)
    print(result)
    
    test_empty = "abc"
    empty_result = extract_digits(test_empty)
    print(empty_result)
    
    test_numbers = "789"
    numbers_only = extract_digits(test_numbers)
    print(numbers_only)