def snake_to_camel(snake_str):
    parts = snake_str.split('_')
    return parts[0] + ''.join(part.capitalize() for part in parts[1:])

if __name__ == '__main__':
    test_cases = [
        ("hello_world", "helloWorld"),
        ("user_name", "userName"),
        ("first_name_last_name", "firstNameLastName"),
        ("a_b_c", "aBC"),
        ("single", "single"),
        ("snake_case_conversion", "snakeCaseConversion"),
    ]
    for input_val, expected in test_cases:
        result = snake_to_camel(input_val)
        print(f"{input_val} -> {result} (Expected: {expected}, Match: {result == expected})")