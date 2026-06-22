class WordLengthChecker:
    MIN_LENGTH = 6

    @staticmethod
    def is_word_long(word):
        return len(word) > WordLengthChecker.MIN_LENGTH

if __name__ == '__main__':
    words = ["hello", "world", "a", "programming"]
    checker = WordLengthChecker()
    print(f"Word 'hello': {checker.is_word_long('hello')}")
    print(f"Word 'world': {checker.is_word_long('world')}")
    print(f"Word 'a': {checker.is_word_long('a')}")
    print(f"Word 'programming': {checker.is_word_long('programming')}")