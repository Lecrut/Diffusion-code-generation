def find_first_word(sentence):
    import re
    words = re.findall(r'\b\w+\b', sentence)
    return words[0] if words else None

if __name__ == '__main__':
    sample_sentence = "  Hello,   world! This is a test. "
    print(find_first_word(sample_sentence))