def normalize_text(text):
    return text.strip()

if __name__ == '__main__':
    sample_text_1 = "   hello world   "
    sample_text_2 = "\n\n\tPython\t\n\n"
    sample_text_3 = "no_spaces"
    print(normalize_text(sample_text_1))
    print(normalize_text(sample_text_2))
    print(normalize_text(sample_text_3))