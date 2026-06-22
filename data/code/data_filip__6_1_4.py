def sanitize_and_convert(text):
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    return '_'.join(text.split(' '))

if __name__ == '__main__':
    sample_data = "This is a sample string with spaces"
    converted_result = sanitize_and_convert(sample_data)
    print(converted_result)