ALPHANUMERIC_PATTERN = '[^a-zA-Z0-9]'

def filter_alphanumeric(input_string):
    filtered_chars = []
    for char in input_string:
        if char.isalnum():
            filtered_chars.append(char)
    return ''.join(filtered_chars)

if __name__ == '__main__':
    sample_input = "Hello, World! 123."
    result = filter_alphanumeric(sample_input)
    print(result)