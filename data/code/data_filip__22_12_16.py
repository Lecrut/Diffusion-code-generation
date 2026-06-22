class RLECompressor:
    def compress(self, text):
        if not text:
            return ""
        result = []
        count = 1
        current_char = text[0]
        for i in range(1, len(text)):
            if text[i] == current_char:
                count += 1
            else:
                result.append(f"{count}{current_char}")
                current_char = text[i]
                count = 1
        result.append(f"{count}{current_char}")
        return "".join(result)

    def decompress(self, compressed_text):
        if not compressed_text:
            return ""
        result = []
        i = 0
        while i < len(compressed_text):
            if not compressed_text[i].isdigit():
                return ""
            j = i
            while j < len(compressed_text) and compressed_text[j].isdigit():
                j += 1
            count = int(compressed_text[i:j])
            if j >= len(compressed_text):
                return ""
            char = compressed_text[j]
            result.append(char * count)
            i = j + 1
        return "".join(result)

if __name__ == '__main__':
    compressor = RLECompressor()
    original = "AAABBBCCDAAA"
    compressed = compressor.compress(original)
    decompressed = compressor.decompress(compressed)
    print(compressed)
    print(decompressed)