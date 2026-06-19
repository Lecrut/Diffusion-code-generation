def remove_spaces(text):
    return text.translate(str.maketrans('', '', ' '))

if __name__ == '__main__':
    sample_text = "This is a sample text with spaces."
    result = remove_spaces(sample_text)
    print(result)