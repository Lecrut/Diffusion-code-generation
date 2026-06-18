class WordCombiner:
    def __init__(self):
        self._cache = {}
    def combine(self, word1: str, word2: str) -> str:
        key = (word1.lower(), word2.lower())
        if key in self._cache:
            return self._cache[key]
        result = f"{word1} {word2}"
        self._cache[key] = result
        return result
if __name__ == '__main__':
    combiner = WordCombiner()
    sample_word_1 = "Hello"
    sample_word_2 = "World"
    combined_result = combiner.combine(sample_word_1, sample_word_2)
    print(combined_result.upper())