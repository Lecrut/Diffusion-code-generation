def check_word_presence(text, target_words):
    text_lower = text.lower()
    word_counts = {word: text_lower.count(word.lower()) for word in target_words}
    return word_counts

if __name__ == '__main__':
    sample_text = "The quick brown fox jumps over the lazy dog fox"
    sample_targets = ["quick", "fox", "lazy", "cat"]
    result = check_word_presence(sample_text, sample_targets)
    print(result)