def remove_spaces(text):
    if not isinstance(text, str):
        raise ValueError('Input must be a string')
    translation_table = str.maketrans('', '', ' ')
    return text.translate(translation_table)
if __name__ == '__main__':
    sample_text1 = 'Hello, World! This is a test.'
    sample_text2 = 'Python programming is fun!'
    sample_text3 = '  Leading and trailing spaces  '
    print(remove_spaces(sample_text1))
    print(remove_spaces(sample_text2))
    print(remove_spaces(sample_text3))