class StringChecker:
    def __init__(self, identifiers: list):
        if not isinstance(identifiers, list) or not all(isinstance(item, str) for item in identifiers):
            raise ValueError("Identifiers must be a list of strings")
        self.identifiers = identifiers

    def contains_identifier(self, target_word: str) -> bool:
        if not isinstance(target_word, str) or not target_word:
            return False
        return any(target_word == identifier for identifier in self.identifiers)

if __name__ == '__main__':
    checker = StringChecker(["apple", "banana", "cherry"])
    word1 = "banana"
    word2 = "grape"
    word3 = ""
    print(f"Does the list contain '{word1}'? {checker.contains_identifier(word1)}")
    print(f"Does the list contain '{word2}'? {checker.contains_identifier(word2)}")
    print(f"Does the list contain an empty string? {checker.contains_identifier(word3)}")