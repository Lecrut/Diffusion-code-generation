def build_dictionary(text):
    words = text.lower()
    cleaned_words = []
    for char in words:
        if 'a' <= char <= 'z' or '0' <= char <= '9':
            cleaned_words.append(char)
    return set(cleaned_words)
if __name__ == '__main__':
    sample_text1 = "Hello world! This is a test sentence, and it contains numbers 123."
    sample_text2 = "Python programming is fun. A simple task."
    print(build_dictionary(sample_text1))
    print(build_dictionary(sample_text2))