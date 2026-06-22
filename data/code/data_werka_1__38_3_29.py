class LetterChecker:
    @staticmethod
    def has_repeated_letters(s):
        return len(s) != len(set(s))

if __name__ == '__main__':
    test_strings = ["hello", "world", "abcde", "programming"]
    for string in test_strings:
        print(f"'{string}' has repeated letters: {LetterChecker.has_repeated_letters(string)}")