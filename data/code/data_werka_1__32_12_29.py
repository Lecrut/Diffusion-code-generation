def calculate_character_count(input_string):
    return len(input_string)

if __name__ == '__main__':
    sample_values = [
        "Hello, World!",
        "Python",
        "",
        "1234567890",
        "Special characters: !@#$%^&*()"
    ]
    
    for value in sample_values:
        print(calculate_character_count(value))