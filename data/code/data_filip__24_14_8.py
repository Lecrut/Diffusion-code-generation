class RunLengthEncoder:
    def __init__(self, data):
        self.original = data
        self.encoded = self._encode(data)

    def _encode(self, string):
        if not string:
            return ""
        encoded = []
        current_char = string[0]
        count = 1
        for char in string[1:]:
            if char == current_char:
                count += 1
            else:
                encoded.append((count, current_char))
                current_char = char
                count = 1
        encoded.append((count, current_char))
        return encoded

    def _decode(self, encoded_data):
        decoded = []
        for count, char in encoded_data:
            decoded.append(char * count)
        return "".join(decoded)

    def get_encoded(self):
        return self.encoded

    def get_decoded(self):
        return self._decode(self.encoded)

if __name__ == "__main__":
    sample_data = "AAAABBBCCDAA"
    encoder = RunLengthEncoder(sample_data)
    print(encoder.get_encoded())
    print(encoder.get_decoded())

    sample_data2 = "XYZZZZ"
    encoder2 = RunLengthEncoder(sample_data2)
    print(encoder2.get_encoded())
    print(encoder2.get_decoded())

    sample_data3 = ""
    encoder3 = RunLengthEncoder(sample_data3)
    print(encoder3.get_encoded())
    print(encoder3.get_decoded())