class BinaryToHexConverter:
    def __init__(self, binary_string):
        self.binary_string = binary_string
        self._validate()

    def _validate(self):
        if not self.binary_string:
            raise ValueError("Input cannot be empty")
        for char in self.binary_string:
            if char not in ('0', '1'):
                raise ValueError(f"Invalid binary character: {char}")

    def convert(self):
        if self.binary_string.startswith('0b'):
            clean_string = self.binary_string[2:]
        else:
            clean_string = self.binary_string
        
        if not clean_string:
            return '0x0'
        
        decimal_value = int(clean_string, 2)
        return hex(decimal_value)

if __name__ == '__main__':
    samples = ["1010", "11111111", "01001010", "123"]
    
    for s in samples:
        try:
            converter = BinaryToHexConverter(s)
            print(f"{s} -> {converter.convert()}")
        except ValueError as e:
            print(f"{s} -> Error: {e}")