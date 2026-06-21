class IdentifierChecker:
    def __init__(self, identifiers: list):
        self.identifiers = identifiers

    def contains(self, target: str) -> bool:
        if not isinstance(target, str):
            raise TypeError("Target must be a string")
        return target in self.identifiers

if __name__ == '__main__':
    identifiers = ["apple", "banana", "cherry"]
    checker1 = IdentifierChecker(identifiers)
    print(f"Contains 'banana': {checker1.contains('banana')}")
    print(f"Contains 'grape': {checker1.contains('grape')}")
    try:
        print(checker1.contains(123))
    except TypeError as e:
        print(e)