def check_words_in_text(word_list, text):
    text_words = set(text.lower().split())
    found_words = set()
    for word in word_list:
        if word.lower() in text_words:
            found_words.add(word)
    return list(found_words)
if __name__ == '__main__':
    sample_word_list = ["apple", "banana", "cherry", "date"]
    sample_text = "This is a sentence about apples and bananas. Dates are sweet."
    result = check_words_in_text(sample_word_list, sample_text)
    print(result)