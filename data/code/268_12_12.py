def extract_first_word(text):
    words = text.strip().split()
    if words:
        return words[0]
    return ""

if __name__ == '__main__':
    sample_text1 = "  This is a test.  "
    sample_text2 = "\tAnother example here.\n"
    sample_text3 = "singleword"
    empty_string = "   "

    print(extract_first_word(sample_text1))
    print(extract_first_word(sample_text2))
    print(extract_first_word(sample_text3))
    print(extract_first_word(empty_string))