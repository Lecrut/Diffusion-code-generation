class RunLengthEncoder:
    def encode(self, data: str) -> str:
        if not data:
            return ""
        encoded = []
        count = 1
        for i in range(1, len(data)):
            if data[i] == data[i - 1]:
                count += 1
            else:
                encoded.append(f"{count}{data[i - 1]}")
                count = 1
        encoded.append(f"{count}{data[-1]}")
        return "".join(encoded)

    def decode(self, data: str) -> str:
        if not data:
            return ""
        decoded = []
        i = 0
        while i < len(data):
            count = 0
            while i < len(data) and data[i].isdigit():
                count = count * 10 + int(data[i])
                i += 1
            if i < len(data):
                decoded.append(data[i] * count)
                i += 1
        return "".join(decoded)

if __name__ == "__main__":
    encoder = RunLengthEncoder()
    original_text = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB"
    encoded_text = encoder.encode(original_text)
    decoded_text = encoder.decode(encoded_text)
    print(f"Original: {original_text}")
    print(f"Encoded: {encoded_text}")
    print(f"Decoded: {decoded_text}")