def check_word_presence(word_list, text):
    text_words = set(text.lower().split())
    for word in word_list:
        if word.lower() in text_words:
            return True
    return False
if __name__ == '__main__':
    sample_word_list = ["apple", "banana", "cherry", "date"]
    sample_text = "This is a sentence about apples and bananas. Dates are sweet."
    result = check_word_presence(sample_word_list, sample_text)
    print(result)