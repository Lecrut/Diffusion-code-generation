class LetterChecker:

    def __init__(self):
        self._seen = set()

    def reset(self):
        self._seen.clear()

    def has_repeated_letters(self, text):
        if not isinstance(text, str):
            raise ValueError('Input must be a string')
        for char in text:
            if char in self._seen:
                return True
            self._seen.add(char)
        return False
if __name__ == '__main__':
    checker = LetterChecker()
    sample_string1 = 'hello world'
    sample_string2 = 'programming'
    print(checker.has_repeated_letters(sample_string1))
    print(checker.has_repeated_letters(sample_string2))
    checker.reset()
    sample_string3 = 'abcdefg'
    sample_string4 = 'aabbccddeeff'
    print(checker.has_repeated_letters(sample_string3))
    print(checker.has_repeated_letters(sample_string4))