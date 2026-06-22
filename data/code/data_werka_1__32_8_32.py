def calculate_string_length(input_string):
    return len(input_string)

if __name__ == '__main__':
    sample_values = [
        "Hello, World!",
        "Python is great.",
        "1234567890",
        "",
        "   ",
        "!@#$%^&*()"
    ]
    
    for value in sample_values:
        print(calculate_string_length(value))