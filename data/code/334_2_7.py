class WordCombiner:
    def combine(self, str1: str, str2: str) -> str:
        return f"{str1}{str2}"
if __name__ == '__main__':
    combiner = WordCombiner()
    result = combiner.combine("Hello", "World")
    print(result)