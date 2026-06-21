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
            count_str = ""
            while i < len(data) and data[i].isdigit():
                count_str += data[i]
                i += 1
            if i < len(data):
                count = int(count_str) if count_str else 1
                decoded.append(data[i] * count)
                i += 1
        return "".join(decoded)

if __name__ == "__main__":
    sample_input = "AAABBBCCCCCDD"
    encoder = RunLengthEncoder()
    encoded_result = encoder.encode(sample_input)
    print(encoded_result)
    decoded_result = encoder.decode(encoded_result)
    print(decoded_result)