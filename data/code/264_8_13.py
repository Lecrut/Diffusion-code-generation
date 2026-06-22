def find_words_with_substring(text, substring):
    WORD_DELIMITERS = " ,.!?"
    words = [word.strip(WORD_DELIMITERS) for word in text.split()]
    return [word for word in words if substring.lower() in word.lower()]

if __name__ == '__main__':
    sample_text = "Hello world, this is a test string with the substring 'test.'"
    sample_substring = 'test'
    result = find_words_with_substring(sample_text, sample_substring)
    print(result)