class RunLengthEncoder:
    @staticmethod
    def compress(data: str) -> str:
        if not data:
            return ""
        encoded = []
        count = 1
        for i in range(1, len(data)):
            if data[i] == data[i - 1]:
                count += 1
            else:
                encoded.append(f"{data[i - 1]}{count}")
                count = 1
        encoded.append(f"{data[-1]}{count}")
        return "".join(encoded)

    @staticmethod
    def decompress(data: str) -> str:
        if not data:
            return ""
        decoded = []
        i = 0
        while i < len(data):
            char = data[i]
            i += 1
            num_str = ""
            while i < len(data) and data[i].isdigit():
                num_str += data[i]
                i += 1
            count = int(num_str) if num_str else 1
            decoded.append(char * count)
        return "".join(decoded)

if __name__ == "__main__":
    sample_input = "WWWWWWWWWWWWBWWWWWWWWWWWWBBB"
    compressed = RunLengthEncoder.compress(sample_input)
    print(compressed)
    decompressed = RunLengthEncoder.decompress(compressed)
    print(decompressed)
    another_input = "AABBCCCD"
    print(RunLengthEncoder.compress(another_input))
    print(RunLengthEncoder.decompress("A3B2C4D1"))