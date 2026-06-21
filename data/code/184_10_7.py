def check_word_presence(text, target_words):
    text_lower = text.lower()
    word_counts = {word: 0 for word in target_words}
    for word in set(target_words):
        if word in text_lower:
            word_counts[word] += text_lower.count(word)
    return word_counts

if __name__ == '__main__':
    sample_text = "The quick brown fox jumps over the lazy dog. Fox and dog are friends."
    sample_targets = ["fox", "dog", "cat", "bird"]
    result = check_word_presence(sample_text, sample_targets)
    print(result)