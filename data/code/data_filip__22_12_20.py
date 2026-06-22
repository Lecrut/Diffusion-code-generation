class RLECompressor:
    def compress(self, data):
        if not isinstance(data, str):
            try:
                data = str(data)
            except Exception:
                return ""
        if not data:
            return ""
        result = []
        current_char = data[0]
        count = 1
        for i in range(1, len(data)):
            if data[i] == current_char:
                count += 1
            else:
                result.append(f"{count}{current_char}")
                current_char = data[i]
                count = 1
        result.append(f"{count}{current_char}")
        return "".join(result)

    def decompress(self, data):
        if not isinstance(data, str):
            try:
                data = str(data)
            except Exception:
                return ""
        if not data:
            return ""
        result = []
        i = 0
        while i < len(data):
            if not data[i].isdigit():
                return ""
            j = i
            while j < len(data) and data[j].isdigit():
                j += 1
            count = int(data[i:j])
            if j >= len(data) or not data[j].isalnum() and data[j] != ' ':
                return ""
            char = data[j]
            result.append(char * count)
            i = j + 1
        return "".join(result)

if __name__ == "__main__":
    compressor = RLECompressor()
    original = "AAABBBCCCCDDDDDD"
    compressed = compressor.compress(original)
    decompressed = compressor.decompress(compressed)
    print(f"Original: {original}")
    print(f"Compressed: {compressed}")
    print(f"Decompressed: {decompressed}")
    test_cases = ["", "A", "AAAA", "ABABAB", "123A", 123, None, ""]
    for case in test_cases:
        try:
            c = compressor.compress(case)
            d = compressor.decompress(c) if c else ""
            print(f"Input: {repr(case)} -> Compressed: {repr(c)} -> Decompressed: {repr(d)}")
        except Exception:
            print(f"Input: {repr(case)} -> Error")