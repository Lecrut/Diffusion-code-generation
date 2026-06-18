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
    unique_words = set()
    for word in words_list:
        if word:
            unique_words.add(word)
    return unique_words
if __name__ == '__main__':
    sample_text = "Hello world! This is a test sentence, and it contains punctuation and capitalization."
    dictionary = build_dictionary(sample_text)
    print(dictionary)