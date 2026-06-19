def remove_spaces(text):
    translation_table = str.maketrans('', '', ' ')
    return text.translate(translation_table)

if __name__ == '__main__':
    sample_text = "Hello World This is a Test"
    result = remove_spaces(sample_text)
    print(result)