class RunLengthEncoder:
    def compress(self, text: str) -> str:
        if not text:
            return ""
        compressed = []
        current_char = text[0]
        count = 1
        for i in range(1, len(text)):
            char = text[i]
            if char == current_char:
                count += 1
            else:
                compressed.append(f"{count}{current_char}")
                current_char = char
                count = 1
        compressed.append(f"{count}{current_char}")
        return "".join(compressed)

    def decompress(self, encoded: str) -> str:
        if not encoded:
            return ""
        decompressed = []
        i = 0
        n = len(encoded)
        while i < n:
            count_str = []
            while i < n and encoded[i].isdigit():
                count_str.append(encoded[i])
                i += 1
            count = int("".join(count_str))
            if i < n:
                char = encoded[i]
                i += 1
                decompressed.append(char * count)
        return "".join(decompressed)

if __name__ == '__main__':
    encoder = RunLengthEncoder()
    test_strings = ["AAABBBCC", "A", "", "AAAAABBBBBCCCCCDD", "XYZ"]
    for s in test_strings:
        compressed = encoder.compress(s)
        decompressed = encoder.decompress(compressed)
        print(f"Original: {s}")
        print(f"Compressed: {compressed}")
        print(f"Decompressed: {decompressed}")
        print("---")