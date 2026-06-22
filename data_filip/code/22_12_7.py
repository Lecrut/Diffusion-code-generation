class RLECompressor:
    def compress(self, data):
        if not data:
            return ""
        result = []
        current_char = data[0]
        count = 1
        for char in data[1:]:
            if char == current_char:
                count += 1
            else:
                result.append(f"{count}{current_char}")
                current_char = char
                count = 1
        result.append(f"{count}{current_char}")
        return "".join(result)

    def decompress(self, data):
        if not data:
            return ""
        result = []
        i = 0
        while i < len(data):
            count = 0
            while i < len(data) and data[i].isdigit():
                count = count * 10 + int(data[i])
                i += 1
            if i < len(data):
                result.append(data[i] * count)
                i += 1
        return "".join(result)

if __name__ == '__main__':
    compressor = RLECompressor()
    original = "AAAABBBCCDAA"
    compressed = compressor.compress(original)
    decompressed = compressor.decompress(compressed)
    print(f"Original: {original}")
    print(f"Compressed: {compressed}")
    print(f"Decompressed: {decompressed}")
    test_input = "12a3b2c12a3b2c"
    print(f"Test Input: {test_input}")
    print(f"Decompressed Test: {compressor.decompress(test_input)}")