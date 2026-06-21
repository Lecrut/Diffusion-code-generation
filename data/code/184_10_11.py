def check_word_presence(text, target_words):
    word_counts = {}
    text_lower = text.lower()
    for word in set(target_words):
        if word in text_lower:
            count = text_lower.count(word)
            word_counts[word] = count
    return word_counts

if __name__ == '__main__':
    sample_text = "The quick brown fox jumps over the lazy dog. Fox is quick."
    target_words_list = ["quick", "fox", "lazy", "cat"]
    result = check_word_presence(sample_text, target_words_list)
    print(result)