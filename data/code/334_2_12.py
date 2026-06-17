class WordCombiner:
    def combine(self, str1: str, str2: str) -> str:
        return f"{str1}{str2}"
if __name__ == '__main__':
    word_combiner = WordCombiner()
    result_a = word_combiner.combine("Hello", "World")
    print(result_a)
    result_b = word_combiner.combine("Python", 3.0)
    print(type(result_b))