class WordCombiner:
    def combine(self, str1: str, str2: str) -> str:
        if not isinstance(str1, str):
            raise TypeError("First argument must be a string")
        if not isinstance(str2, str):
            raise TypeError("Second argument must be a string")
        combined = f"{str1} {str2}"
        return combined
if __name__ == '__main__':
    combiner = WordCombiner()
    result = combiner.combine("Hello", "World")
    print(result)