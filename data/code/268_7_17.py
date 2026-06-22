MAX_WORDS_TO_SPLIT = 1

def extract_first_word(text):
    words = text.split(None, MAX_WORDS_TO_SPLIT)
    if words:
        return words[0]
    else:
        return ""

if __name__ == '__main__':
    sample_string1 = "This is a sample sentence"
    result1 = extract_first_word(sample_string1)
    print(result1)
    sample_string2 = "  leading spaces and multiple words"
    result2 = extract_first_word(sample_string2)
    print(result2)
    sample_string3 = "singleword"
    result3 = extract_first_word(sample_string3)
    print(result3)
    sample_string4 = ""
    result4 = extract_first_word(sample_string4)
    print(result4)