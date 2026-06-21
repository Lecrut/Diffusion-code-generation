def remove_spaces(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string")
    
    translation_table = str.maketrans('', '', ' ')
    return text.translate(translation_table)

if __name__ == '__main__':
    sample_text = "This is yet another variant with spaces."
    try:
        result = remove_spaces(sample_text)
        print(result)
    except ValueError as e:
        print(e)