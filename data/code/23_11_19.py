class RunLengthEncoder:
    def encode(self, data: str) -> str:
        if not data:
            return ""

        encoded = []
        count = 1
        length = len(data)

        for i in range(1, length):
            if data[i] == data[i - 1]:
                count += 1
            else:
                encoded.append(f"{count}{data[i - 1]}")
                count = 1

        encoded.append(f"{count}{data[-1]}")
        return "".join(encoded)

if __name__ == "__main__":
    encoder = RunLengthEncoder()
    sample_string = "AAABBBCCD"
    result = encoder.encode(sample_string)
    print(result)