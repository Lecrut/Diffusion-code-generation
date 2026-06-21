class KeywordSearcher:
    @staticmethod
    def check_word_presence(text, target_words):
        word_counts = {}
        text_lower = text.lower()
        for word in set(target_words):
            if word in text_lower.split():
                word_counts[word] = text_lower.count(word)
        return word_counts

if __name__ == '__main__':
    sample_text = "The quick brown fox jumps over the lazy dog fox"
    sample_targets = ["quick", "fox", "lazy", "cat"]
    searcher = KeywordSearcher()
    result = searcher.check_word_presence(sample_text, sample_targets)
    print(result)