def format_string(text):
    transformations = {
        'lower': text.lower(),
        'upper': text.upper(),
        'title': text.title()
    }
    return transformations

if __name__ == '__main__':
    sample_string = "This is a Test String for Formatting."
    result = format_string(sample_string)
    print(f"Original: {sample_string}")
    print(f"Lowercase: {result['lower']}")
    print(f"Uppercase: {result['upper']}")
    print(f"Title Case: {result['title']}")