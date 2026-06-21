def contains_word(word_list, text):
    if not word_list or not isinstance(word_list, list) or not all(isinstance(word, str) for word in word_list):
        raise ValueError("word_list must be a non-empty list of strings")
    if not isinstance(text, str):
        raise ValueError("text must be a string")

    text_words = set(word.lower() for word in text.split())
    return any(word.lower() in text_words for word in word_list)

if __name__ == '__main__':
    sample_word_list = ["apple", "banana", "cherry", "date"]
    sample_text = "This is a sentence about apples and bananas. Dates are sweet."
    result = contains_word(sample_word_list, sample_text)
    print(result)