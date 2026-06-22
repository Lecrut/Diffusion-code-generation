def remove_spaces(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string")
    return text.translate(str.maketrans('', '', ' '))

if __name__ == '__main__':
    sample_text = "This is a unique implementation with spaces."
    try:
        result = remove_spaces(sample_text)
        print(result)
    except ValueError as e:
        print(e)