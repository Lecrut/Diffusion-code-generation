class IdentifierChecker:
    def __init__(self, identifiers):
        self.identifiers = identifiers if isinstance(identifiers, list) else []

    def contains_identifier(self, target_word):
        return target_word in self.identifiers

if __name__ == '__main__':
    checker = IdentifierChecker(["apple", "banana", "cherry"])
    print(f"Contains 'banana': {checker.contains_identifier('banana')}")
    print(f"Contains 'orange': {checker.contains_identifier('orange')}")
    print(f"Contains 'apple': {checker.contains_identifier('apple')}")