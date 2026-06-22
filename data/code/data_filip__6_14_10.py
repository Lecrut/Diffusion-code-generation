def replace_spaces_with_underscores(text):
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    return text.replace(" ", "_")

if __name__ == '__main__':
    sample_text = "Hello World Python"
    result = replace_spaces_with_underscores(sample_text)
    print(result)