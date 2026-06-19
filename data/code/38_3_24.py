class LetterChecker:
    def __init__(self, string):
        self.string = string

    def has_repeated_letters(self):
        return len(self.string) != len(set(self.string))

if __name__ == '__main__':
    checker1 = LetterChecker("hello")
    checker2 = LetterChecker("world")
    checker3 = LetterChecker("abcde")
    checker4 = LetterChecker("programming")

    print(f"'{checker1.string}': {checker1.has_repeated_letters()}")
    print(f"'{checker2.string}': {checker2.has_repeated_letters()}")
    print(f"'{checker3.string}': {checker3.has_repeated_letters()}")
    print(f"'{checker4.string}': {checker4.has_repeated_letters()}")