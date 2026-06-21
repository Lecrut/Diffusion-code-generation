def validate_input(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string")

def split_by_whitespace(text):
    validate_input(text)
    return text.split()

if __name__ == '__main__':
    sample_text = "Hello World This is a test"
    result = split_by_whitespace(sample_text)
    print(result)