class WordCombiner:
    def combine(self, s1: str, s2: str) -> str:
        return f"{s1} {s2}"
if __name__ == '__main__':
    combiner = WordCombiner()
    result = combiner.combine("Hello", "World")
    print(result)