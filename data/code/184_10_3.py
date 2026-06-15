def check_word_presence(text, target_words):
    word_counts = {}
    text_lower = text.lower()
    for word in target_words:
        word_lower = word.lower()
        if word_lower in text_lower:
            count = text_lower.count(word_lower)
            if word_lower not in word_counts:
                word_counts[word_lower] = 0
            word_counts[word_lower] += count
    return word_counts
if __name__ == '__main__':
    sample_text = "The quick brown fox jumps over the lazy dog. Fox and dog are friends."
    target_words = ["fox", "dog", "cat", "bird"]
    result = check_word_presence(sample_text, target_words)
    print(result)