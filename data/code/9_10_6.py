def remove_whitespace(text):
    return text.strip()

if __name__ == '__main__':
    sample_1 = "   hello world   "
    sample_2 = "\n\tPython Code\n\t"
    sample_3 = "NoSpaces"
    sample_4 = "   "
    
    result_1 = remove_whitespace(sample_1)
    result_2 = remove_whitespace(sample_2)
    result_3 = remove_whitespace(sample_3)
    result_4 = remove_whitespace(sample_4)
    
    print(repr(result_1))
    print(repr(result_2))
    print(repr(result_3))
    print(repr(result_4))