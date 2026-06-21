def contains_word(word_list, text):
    words_set = set(text.lower().split())
    return any(word.lower() in words_set for word in word_list)

if __name__ == '__main__':
    sample_word_list = ["apple", "banana", "cherry", "date"]
    sample_text = "This is a sentence about apples and bananas. Dates are sweet."
    result = contains_word(sample_word_list, sample_text)
    print(result)