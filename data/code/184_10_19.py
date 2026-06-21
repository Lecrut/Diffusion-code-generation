TARGET_WORDS = ["quick", "fox", "lazy", "cat"]
SAMPLE_TEXT = "The quick brown fox jumps over the lazy dog fox"

def check_word_presence(text, target_words):
    word_counts = {}
    text_lower = text.lower()
    for word in set(target_words):
        if word in text_lower.split():
            word_counts[word] = text_lower.count(word)
    return word_counts

if __name__ == '__main__':
    result = check_word_presence(SAMPLE_TEXT, TARGET_WORDS)
    print(result)