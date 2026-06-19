def remove_spaces(text):
    translation_table = str.maketrans('', '', ' \t\n\r\x0b\x0c')
    return text.translate(translation_table)

if __name__ == '__main__':
    sample_text = "This is a sample text with spaces."
    result = remove_spaces(sample_text)
    print(result)