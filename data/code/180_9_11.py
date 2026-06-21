class IdentifierChecker:
    def __init__(self, identifiers):
        self.identifiers = set(identifiers) if identifiers else set()

    def contains(self, target):
        return target in self.identifiers

if __name__ == '__main__':
    checker = IdentifierChecker(["apple", "banana", "cherry"])
    identifier1 = "banana"
    identifier2 = "date"
    print(f"Does '{identifier1}' exist? {checker.contains(identifier1)}")
    print(f"Does '{identifier2}' exist? {checker.contains(identifier2)}")