class WordCombiner:
    def combine(self, string1: str, string2: str) -> str:
        return f"{string1} {string2}"
if __name__ == '__main__':
    combiner = WordCombiner()
    result = combiner.combine("Hello", "World")
    print(result)