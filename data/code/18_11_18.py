class RunLengthEncoder:
    def __init__(self, data=None):
        self.data = data if data is not None else ""

    @staticmethod
    def compress(data):
        if not data:
            return ""
        compressed = []
        current_char = data[0]
        count = 1
        for char in data[1:]:
            if char == current_char:
                count += 1
            else:
                compressed.append(f"{count}{current_char}")
                current_char = char
                count = 1
        compressed.append(f"{count}{current_char}")
        return "".join(compressed)

    @staticmethod
    def decompress(compressed):
        if not compressed:
            return ""
        decompressed = []
        i = 0
        while i < len(compressed):
            num_str = ""
            while i < len(compressed) and compressed[i].isdigit():
                num_str += compressed[i]
                i += 1
            if num_str:
                count = int(num_str)
                char = compressed[i]
                decompressed.append(char * count)
                i += 1
            else:
                break
        return "".join(decompressed)

    def encode(self):
        return RunLengthEncoder.compress(self.data)

    def decode(self, compressed_data):
        return RunLengthEncoder.decompress(compressed_data)

if __name__ == "__main__":
    encoder = RunLengthEncoder()
    test_cases = [
        "aaabbc",
        "aabbbcccc",
        "xyz",
        "",
        "a" * 100
    ]
    for case in test_cases:
        encoded = encoder.encode(case)
        decoded = encoder.decode(encoded)
        print(f"Original: {case[:20]}{'...' if len(case) > 20 else ''}")
        print(f"Encoded:  {encoded}")
        print(f"Decoded:  {decoded[:20]}{'...' if len(case) > 20 else ''}")
        print(f"Match: {case == decoded}")
        print()