class KeywordSearcher:
    def __init__(self, target_words):
        self.target_words = set(target_words.lower())

    @staticmethod
    def _count_word_occurrences(text, word):
        return text.lower().count(word)

    def find_keywords(self, text):
        results = {}
        for word in self.target_words:
            if word in text.lower():
                results[word] = self._count_word_occurrences(text, word)
        return results

if __name__ == '__main__':
    sample_text = "The quick brown fox jumps over the lazy dog. Fox and dog are friends."
    target_words = ["fox", "dog", "cat", "bird"]
    searcher = KeywordSearcher(target_words)
    result = searcher.find_keywords(sample_text)
    print(result)