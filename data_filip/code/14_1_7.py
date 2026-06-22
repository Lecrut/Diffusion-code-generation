def has_unique_chars(s):
    if len(s) > 128:
        return False
    bit_vector = 0
    for char in s:
        val = ord(char)
        if (bit_vector & (1 << val)) > 0:
            return False
        bit_vector |= (1 << val)
    return True

class BitwiseChecker:
    def __init__(self, text):
        self.text = text

    def check(self):
        if len(self.text) > 128:
            return False
        bit_vector = 0
        for char in self.text:
            val = ord(char)
            if (bit_vector & (1 << val)) > 0:
                return False
            bit_vector |= (1 << val)
        return True

if __name__ == '__main__':
    sample_strings = ["abcdefg", "hello", "world", "1234567890abcdefgH"]
    for s in sample_strings:
        result = has_unique_chars(s)
        print(result)

    checker = BitwiseChecker("unique")
    print(checker.check())