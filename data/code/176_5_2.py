def extract_alphabetic_words(text):
    words = []
    current_word = ""
    for char in text:
        if 'a' <= char <= 'z' or 'A' <= char <= 'Z':
            current_word += char
        else:
            if current_word:
                words.append(current_word)
                current_word = ""
    if current_word:
        words.append(current_word)
    return words
if __name__ == '__main__':
    sample_string = "Hello world! 123 Python is fun, and this is a test."
    result = extract_alphabetic_words(sample_string)
    print(result)