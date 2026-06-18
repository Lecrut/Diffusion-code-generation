class WordCombiner:
    def combine(self, str1: str, str2: str) -> str:
        return f"{str1} {str2}".strip()
if __name__ == '__main__':
    word_combiner = WordCombiner()
    result = word_combiner.combine("Hello", "World")
    print(result if result else "")