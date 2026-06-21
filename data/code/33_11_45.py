def remove_spaces(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string")
    translation_table = str.maketrans('', '', ' ')
    return text.translate(translation_table)

if __name__ == '__main__':
    sample_text1 = "Hello World! This is a test."
    sample_text2 = "NoSpacesHere"
    sample_text3 = "   Leading and trailing spaces   "
    
    result1 = remove_spaces(sample_text1)
    result2 = remove_spaces(sample_text2)
    result3 = remove_spaces(sample_text3)
    
    print(result1)
    print(result2)
    print(result3)