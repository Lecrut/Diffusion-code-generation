def check_words_in_text(word_list, text):
    text_words = set(text.lower().split())
    found_words = set()
    for word in word_list:
        if word.lower() in text_words:
            found_words.add(word)
    return list(found_words)
if __name__ == '__main__':
    sample_word_list = ["apple", "banana", "cherry", "date"]
    sample_text = "This is an apple and a banana. Cherry is red. Date is sweet."
    result = check_words_in_text(sample_word_list, sample_text)
    print(result)