class CharacterUniquenessChecker:
    def __init__(self, input_string):
        self.input_string = input_string
        self._validate()

    def _validate(self):
        if not isinstance(self.input_string, str):
            raise TypeError("Input must be a string")
        if not all(ord(c) < 128 for c in self.input_string):
            raise ValueError("Input must contain only ASCII characters")

    def has_unique_characters(self):
        if len(self.input_string) > 128:
            return False
        seen = 0
        for char in self.input_string:
            code = ord(char)
            bit_mask = 1 << code
            if seen & bit_mask:
                return False
            seen |= bit_mask
        return True

if __name__ == '__main__':
    checker = CharacterUniquenessChecker("abcdefg")
    result = checker.has_unique_characters()
    print(result)
    checker2 = CharacterUniquenessChecker("abca")
    result2 = checker2.has_unique_characters()
    print(result2)