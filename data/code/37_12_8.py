class StringCombiner:
    def combine(self, str1: str, str2: str) -> str:
        """Efficiently joins two input strings into a single string."""
        return f"{str1}{str2}"

if __name__ == '__main__':
    combiner = StringCombiner()
    result = combiner.combine("Hello", "World")
    print(result)