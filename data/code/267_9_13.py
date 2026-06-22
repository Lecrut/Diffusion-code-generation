class WordChecker:
    def __init__(self, min_length=10):
        self.min_length = min_length

    def is_long(self, word):
        return len(word) > self.min_length

if __name__ == '__main__':
    checker = WordChecker()
    print(checker.is_long("short"))
    print(checker.is_long("thisisalongstring"))
    print(checker.is_long("onlyletters"))
    print(checker.is_long("this has a space"))
    print(checker.is_long("abcdefghij"))
    print(checker.is_long("a" * 11))
    print(checker.is_long("1234567890"))