def remove_spaces(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string")
    SPACE = ' '
    translation_table = str.maketrans('', '', SPACE)
    return text.translate(translation_table)

if __name__ == '__main__':
    SAMPLE_TEXT1 = "This is a sample text with spaces."
    SAMPLE_TEXT2 = "Another example of removing spaces."
    SAMPLE_TEXT3 = "Yet another variant with multiple spaces."
    
    try:
        print(remove_spaces(SAMPLE_TEXT1))
        print(remove_spaces(SAMPLE_TEXT2))
        print(remove_spaces(SAMPLE_TEXT3))
    except ValueError as e:
        print(e)