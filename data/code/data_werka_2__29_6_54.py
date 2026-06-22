def reverse_string(input_string):
    if not isinstance(input_string, str):
        raise ValueError("Input must be a string")
    return input_string[::-1]

if __name__ == '__main__':
    sample_values = [
        "hello",
        "world",
        "Python",
        "12345",
        "!@#$%"
    ]
    
    for value in sample_values:
        try:
            reversed_value = reverse_string(value)
            print(reversed_value)
        except ValueError as e:
            print(e)