def strip_spaces(input_string):
    return input_string.replace(' ', '')

if __name__ == '__main__':
    original_text = "  Hello World! This is a test.  "
    cleaned_text = strip_spaces(original_text)
    print(cleaned_text)