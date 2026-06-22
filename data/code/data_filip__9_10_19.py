WHITESPACE_CHARS = ' \t\n\r\x0b\x0c'

def strip_whitespace(text):
    cleaned = text.strip(WHITESPACE_CHARS)
    return cleaned

if __name__ == '__main__':
    sample_text = "  \t  Python Programming  \n  "
    output_result = strip_whitespace(sample_text)
    print(output_result)
    
    another_text = "\r\n   Hello World   \t\n"
    second_result = strip_whitespace(another_text)
    print(second_result)
    
    clean_text = "NoSpaces"
    third_result = strip_whitespace(clean_text)
    print(third_result)
    
    empty_text = ""
    fourth_result = strip_whitespace(empty_text)
    print(repr(fourth_result))
    
    only_spaces = "     "
    fifth_result = strip_whitespace(only_spaces)
    print(repr(fifth_result))