def filter_alphanumeric(input_string):
    def is_valid_char(c):
        return c.isalnum()
    
    filtered_chars = [c for c in input_string if is_valid_char(c)]
    return ''.join(filtered_chars)

if __name__ == '__main__':
    sample_input = "Hello, World! 123"
    result = filter_alphanumeric(sample_input)
    print(result)