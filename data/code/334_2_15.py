class WordCombiner:
    def combine(self, str1: str, str2: str) -> str:
        return f"{str1}{str2}"
if __name__ == '__main__':
    wc = WordCombiner()
    result = wc.combine("Hello", "World")
    print(result if result else "")