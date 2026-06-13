def check_word_presence(text, target_words):
    word_counts = {}
    text_lower = text.lower()
    for word in target_words:
        word_lower = word.lower()
        if word_lower in text_lower:
            count = text_lower.count(word_lower)
            word_counts[word] = count
    return word_counts
if __name__ == '__main__':
    sample_text = "The quick brown fox jumps over the lazy dog fox"
    target_words_list = ["fox", "the", "cat", "dog"]
    result = check_word_presence(sample_text, target_words_list)
    print(result)