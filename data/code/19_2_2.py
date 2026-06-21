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

    def decompress(self, compressed):
        if not compressed:
            return ""
        result = []
        i = 0
        while i < len(compressed):
            count = 0
            while i < len(compressed) and compressed[i].isdigit():
                count = count * 10 + int(compressed[i])
                i += 1
            if i < len(compressed):
                char = compressed[i]
                i += 1
                result.append(char * count)
        return "".join(result)

if __name__ == '__main__':
    compressor = RLECompressor()
    sample_input = "AAABBBCCCDDDEEE"
    compressed = compressor.compress(sample_input)
    decompressed = compressor.decompress(compressed)
    print(compressed)
    print(decompressed)
    sample_empty = ""
    compressed_empty = compressor.compress(sample_empty)
    decompressed_empty = compressor.decompress(compressed_empty)
    print(compressed_empty)
    print(decompressed_empty)
    sample_single = "A"
    compressed_single = compressor.compress(sample_single)
    decompressed_single = compressor.decompress(compressed_single)
    print(compressed_single)
    print(decompressed_single)