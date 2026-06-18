def build_dictionary(text):
    words = text.lower()
    cleaned_words = []
    for char in words:
        if 'a' <= char <= 'z' or char == ' ':
            cleaned_words.append(char)
    words_list = []
    current_word = ""
    for char in text:
        if 'a' <= char <= 'z' or char == ' ':
            current_word += char
        else:
            if current_word:
                words_list.append(current_word)
                current_word = ""
    if current_word:
        words_list.append(current_word)
    unique_words = set(word for word in words_list if word)
    return unique_words
if __name__ == '__main__':
    sample_text1 = "Hello world! This is a test sentence, and it contains punctuation."
    sample_text2 = "Programming is fun. Python is powerful and easy to learn."
    sample_text3 = "  Multiple   spaces and  punctuation? Yes!"
    dict1 = build_dictionary(sample_text1)
    print(f"Dictionary for '{sample_text1}': {dict1}")
    dict2 = build_dictionary(sample_text2)
    print(f"Dictionary for '{sample_text2}': {dict2}")
    dict3 = build_dictionary(sample_text3)
    print(f"Dictionary for '{sample_text3}': {dict3}")