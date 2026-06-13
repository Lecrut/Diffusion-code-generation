def process_string(text):
    words_with_case = []
    words_lowercase = []
    for word in text.split():
        words_with_case.append(word)
        words_lowercase.append(word.lower())
    return words_with_case, words_lowercase
if __name__ == '__main__':
    sample_string = "Hello World this is a test"
    words_original, words_lower = process_string(sample_string)
    print("Original Words:", words_original)
    print("Lowercase Words:", words_lower)