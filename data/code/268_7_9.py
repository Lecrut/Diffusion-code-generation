def extract_first_word(text):
    words = text.split()
    return words[0] if words else ""

if __name__ == '__main__':
    sample_string1 = "This is a sample sentence"
    print(extract_first_word(sample_string1))
    sample_string2 = "  leading spaces and multiple words"
    print(extract_first_word(sample_string2))
    sample_string3 = "singleword"
    print(extract_first_word(sample_string3))
    sample_string4 = ""
    print(extract_first_word(sample_string4))