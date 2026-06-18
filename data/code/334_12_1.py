class WordCombiner:
    def combine(self, word1: str, word2: str) -> str:
        return f"{word1} {word2}"
if __name__ == '__main__':
    combiner = WordCombiner()
    result = combiner.combine("Hello", "World")
    print(result)