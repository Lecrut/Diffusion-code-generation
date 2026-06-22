def strip_whitespace(text):
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    return text.strip()

if __name__ == '__main__':
    sample_1 = "   Hello World   "
    sample_2 = "\t\nPython Script\r"
    sample_3 = "NoSpaces"
    sample_4 = "   "
    sample_5 = ""
    print(strip_whitespace(sample_1))
    print(strip_whitespace(sample_2))
    print(strip_whitespace(sample_3))
    print(strip_whitespace(sample_4))
    print(strip_whitespace(sample_5))