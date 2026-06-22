class CharacterComparator:
    def compare(self, phrase1: str, phrase2: str) -> bool:
        return set(phrase1) == set(phrase2)

if __name__ == '__main__':
    comparator = CharacterComparator()
    result1 = comparator.compare("listen", "silent")
    result2 = comparator.compare("hello", "world")
    print(result1)
    print(result2)