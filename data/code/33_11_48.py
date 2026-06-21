SPACE_CHAR = ' '

def remove_spaces(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string")
    translation_table = str.maketrans('', '', SPACE_CHAR)
    return text.translate(translation_table)

if __name__ == '__main__':
    sample_text1 = "This is a fresh variant with spaces."
    sample_text2 = 'Another example without any spaces.'
    sample_text3 = "Yet another implementation with multiple spaces."
    
    try:
        print(remove_spaces(sample_text1))
        print(remove_spaces(sample_text2))
        print(remove_spaces(sample_text3))
    except ValueError as e:
        print(e)