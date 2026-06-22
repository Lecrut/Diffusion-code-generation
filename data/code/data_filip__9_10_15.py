import textwrap

def remove_whitespace(input_string):
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    return input_string.strip()

if __name__ == '__main__':
    sample_with_spaces = "   hello world   "
    sample_with_tabs = "\t\n\tPython Code\n\t"
    sample_clean = "CleanString"
    
    result_1 = remove_whitespace(sample_with_spaces)
    result_2 = remove_whitespace(sample_with_tabs)
    result_3 = remove_whitespace(sample_clean)
    
    print(result_1)
    print(result_2)
    print(result_3)