def calculate_string_length(input_string):
    return len(input_string)

if __name__ == '__main__':
    sample_values = [
        "Hello, World!",
        "Python programming",
        "1234567890",
        "!@#$%^&*()",
        " "
    ]
    
    for value in sample_values:
        result = calculate_string_length(value)
        print(result)