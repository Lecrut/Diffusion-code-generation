class HexConverter:
    def __init__(self):
        self.char_to_val = {}
        for i in range(10):
            self.char_to_val[chr(ord('0') + i)] = i
        for i in range(10, 16):
            self.char_to_val[chr(ord('A') + i - 10)] = i
            self.char_to_val[chr(ord('a') + i - 10)] = i

    def convert(self, hex_string):
        negative = False
        if hex_string.startswith('-'):
            negative = True
            hex_string = hex_string[1:]
        elif hex_string.startswith('+'):
            hex_string = hex_string[1:]
        result = 0
        for char in hex_string:
            result = result * 16 + self.char_to_val[char]
        return -result if negative else result

if __name__ == '__main__':
    converter = HexConverter()
    print(converter.convert("1a3f"))
    print(converter.convert("FF"))
    print(converter.convert("0"))
    print(converter.convert("deadBEEF"))
    print(converter.convert("-42"))