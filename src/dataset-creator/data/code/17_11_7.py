def build_dictionary(text):
    words = text.lower()
    cleaned_text = ""
    for char in words:
        if 'a' <= char <= 'z' or '0' <= char <= '9':
            cleaned_text += char
    words = cleaned_text.split()
    word_set = set(words)
    return word_set
if __name__ == '__main__':
    sample_text = "Hello world! This is a test sentence, and it contains punctuation and capitalization."
    dictionary = build_dictionary(sample_text)
    print(dictionary)