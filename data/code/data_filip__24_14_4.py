class RLEngine:
    def __init__(self, data):
        self.data = data

    def encode(self):
        if not self.data:
            return []
        encoded = []
        current_char = self.data[0]
        count = 1
        for char in self.data[1:]:
            if char == current_char:
                count += 1
            else:
                encoded.append(f"{count}{current_char}")
                current_char = char
                count = 1
        encoded.append(f"{count}{current_char}")
        return encoded

    def decode(self, encoded_data):
        decoded = []
        for item in encoded_data:
            count = int(item[:-1])
            char = item[-1]
            decoded.append(char * count)
        return "".join(decoded)

if __name__ == "__main__":
    engine = RLEngine("AAABBBCCD")
    encoded = engine.encode()
    print(encoded)
    decoded = engine.decode(encoded)
    print(decoded)