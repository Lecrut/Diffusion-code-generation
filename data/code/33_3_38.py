import string

def filter_alphanumeric(input_string):
    allowed_chars = set(string.ascii_letters + string.digits)
    return ''.join(char for char in input_string if char in allowed_chars)

if __name__ == '__main__':
    sample_input = "Hello, World! 123"
    result = filter_alphanumeric(sample_input)
    print(result)