class BinaryConverter:
    __slots__ = ('_value',)

    def __init__(self, binary_input):
        if not binary_input:
            self._value = 0
            return
        valid_chars = frozenset('01')
        if not all(c in valid_chars for c in binary_input):
            raise ValueError("Input must contain only binary digits")
        self._value = int(binary_input, 2)

    def to_hexadecimal(self, uppercase=True):
        fmt = 'X' if uppercase else 'x'
        return format(self._value, fmt)

    def to_hexadecimal_chunked(self, chunk_size=4):
        val = self._value
        if val == 0:
            return "0"
        hex_digits = []
        mask = (1 << chunk_size) - 1
        while val > 0:
            digit = val & mask
            if digit < 10:
                hex_digits.append(chr(ord('0') + digit))
            else:
                hex_digits.append(chr(ord('A') + digit - 10))
            val >>= chunk_size
        return "".join(reversed(hex_digits))

if __name__ == '__main__':
    test_cases = ["11110000", "1010101010101010", "0", "11111111111111111111"]
    converter = BinaryConverter(test_cases[0])
    print(converter.to_hexadecimal())
    converter2 = BinaryConverter(test_cases[1])
    print(converter2.to_hexadecimal_chunked(4))
    for bin_str in test_cases[2:]:
        c = BinaryConverter(bin_str)
        print(c.to_hexadecimal())