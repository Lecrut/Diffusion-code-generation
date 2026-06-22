class RLECompressor:
    def compress(self, text):
        if not text:
            return ""
        compressed = []
        count = 1
        length = len(text)
        for i in range(length):
            if i + 1 < length and text[i] == text[i + 1]:
                count += 1
            else:
                compressed.append(f"{count}{text[i]}")
                count = 1
        return "".join(compressed)

    def decompress(self, text):
        if not text:
            return ""
        decompressed = []
        i = 0
        while i < len(text):
            count_str = ""
            while i < len(text) and text[i].isdigit():
                count_str += text[i]
                i += 1
            if i < len(text):
                char = text[i]
                count = int(count_str)
                decompressed.append(char * count)
                i += 1
        return "".join(decompressed)

if __name__ == "__main__":
    compressor = RLECompressor()
    original = "aaabbccccdd"
    compressed = compressor.compress(original)
    decompressed = compressor.decompress(compressed)
    print(f"Original: {original}")
    print(f"Compressed: {compressed}")
    print(f"Decompressed: {decompressed}")
    print(f"Round-trip match: {original == decompressed}")
    print(f"Empty input compress: '{compressor.compress('')}'")
    print(f"Empty input decompress: '{compressor.decompress('')}'")
    print(f"Single char compress: '{compressor.compress('z')}'")
    print(f"Single char decompress: '{compressor.decompress('1z')}'")
    print(f"Mixed compress: '{compressor.compress('a1b2c3')}'")
    print(f"Mixed decompress: '{compressor.decompress('1a11b1c11d')}'")