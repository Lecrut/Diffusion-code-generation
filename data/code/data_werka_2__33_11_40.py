def validate_input(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string")

def remove_spaces(text):
    validate_input(text)
    translation_table = str.maketrans('', '', ' ')
    return text.translate(translation_table)

if __name__ == '__main__':
    sample_text1 = "This is a sample text with spaces."
    sample_text2 = 'Another example without any spaces.'
    sample_text3 = "Yet another variant with multiple spaces."

    try:
        print(remove_spaces(sample_text1))
        print(remove_spaces(sample_text2))
        print(remove_spaces(sample_text3))
    except ValueError as e:
        print(e)