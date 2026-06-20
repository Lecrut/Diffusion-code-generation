def normalize_text(text):
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    return text.strip()

if __name__ == '__main__':
    sample_1 = "   Hello World   "
    sample_2 = "NoSpaces"
    sample_3 = "\t\tTabbedText\n\n"
    print(normalize_text(sample_1))
    print(normalize_text(sample_2))
    print(normalize_text(sample_3))