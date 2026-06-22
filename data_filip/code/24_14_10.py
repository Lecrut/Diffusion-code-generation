class RunLengthEncoder:
    def __init__(self, data: str = ""):
        self.data = data

    def encode(self, data: str = None) -> str:
        if data is not None:
            self.data = data
        if not self.data:
            return ""
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
        return "".join(encoded)

    def decode(self, encoded: str = None) -> str:
        if encoded is not None:
            encoded_data = encoded
        else:
            encoded_data = self.encode()
        if not encoded_data:
            return ""
        decoded = []
        i = 0
        while i < len(encoded_data):
            count_str = ""
            while i < len(encoded_data) and encoded_data[i].isdigit():
                count_str += encoded_data[i]
                i += 1
            if i < len(encoded_data):
                char = encoded_data[i]
                i += 1
                count = int(count_str) if count_str else 1
                decoded.append(char * count)
        return "".join(decoded)

if __name__ == "__main__":
    encoder = RunLengthEncoder("WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW")
    encoded = encoder.encode()
    print(encoded)
    decoded = encoder.decode(encoded)
    print(decoded)

    encoder2 = RunLengthEncoder("AABCCCDEEEE")
    encoded2 = encoder2.encode()
    print(encoded2)
    decoded2 = encoder2.decode(encoded2)
    print(decoded2)

    encoder3 = RunLengthEncoder("")
    encoded3 = encoder3.encode()
    print(encoded3)
    decoded3 = encoder3.decode(encoded3)
    print(decoded3)