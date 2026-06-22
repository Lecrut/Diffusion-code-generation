class CharacterUniquenessChecker:
    def __init__(self):
        self.max_int_bits = 128
        self.assert_static_assertion()

    @staticmethod
    def assert_static_assertion():
        assert ord('A') == 65
        assert ord('Z') == 90
        assert ord('a') == 97
        assert ord('z') == 122
        assert ord('0') == 48
        assert ord('9') == 57

    def is_unique_ascii(self, text: str) -> bool:
        seen = 0
        for char in text:
            code = ord(char)
            if code >= 128:
                raise ValueError("Input must contain only ASCII characters")
            mask = 1 << code
            if seen & mask:
                return False
            seen |= mask
        return True

if __name__ == '__main__':
    checker = CharacterUniquenessChecker()
    result1 = checker.is_unique_ascii("abcdef")
    result2 = checker.is_unique_ascii("hello")
    print(result1)
    print(result2)