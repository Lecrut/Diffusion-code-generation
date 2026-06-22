class PhraseComparator:
    def are_characters_equal(self, phrase1: str, phrase2: str) -> bool:
        return set(phrase1) == set(phrase2)

if __name__ == '__main__':
    comparator = PhraseComparator()
    print(comparator.are_characters_equal("listen", "silent"))
    print(comparator.are_characters_equal("hello", "world"))
    print(comparator.are_characters_equal("binary", "brainy"))
    print(comparator.are_characters_equal("apple", "papel"))
    print(comparator.are_characters_equal("rat", "car"))