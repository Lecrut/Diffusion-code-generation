def build_dictionary(text):
    words = text.lower()
    cleaned_words = []
    for char in words:
        if 'a' <= char <= 'z' or '0' <= char <= '9':
            cleaned_words.append(char)
    return set(cleaned_words)
if __name__ == '__main__':
    sample_text1 = "Hello world! This is a test sentence, and it contains punctuation."
    sample_text2 = "Python programming is fun. Programming is powerful."
    sample_text3 = "A B C. a b c"
    dict1 = build_dictionary(sample_text1)
    print(f"Dictionary for '{sample_text1}': {dict1}")
    dict2 = build_dictionary(sample_text2)
    print(f"Dictionary for '{sample_text2}': {dict2}")
    dict3 = build_dictionary(sample_text3)
    print(f"Dictionary for '{sample_text3}': {dict3}")