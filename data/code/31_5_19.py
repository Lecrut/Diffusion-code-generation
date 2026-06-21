class HexDecoder:
    def __init__(self, hex_string):
        self.value = int(hex_string, 16)

    def get_decimal(self):
        return self.value

if __name__ == '__main__':
    sample = "1A3F"
    decoder = HexDecoder(sample)
    print(decoder.get_decimal())