def split_by_whitespace(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string")
    
    return text.split()

if __name__ == '__main__':
    sample_text = "Hello World This is a test"
    result = split_by_whitespace(sample_text)
    print(result)