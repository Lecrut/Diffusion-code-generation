class RunLengthEncoder:
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
                result.append(str(count) + current_char)
                current_char = text[i]
                count = 1
        result.append(str(count) + current_char)
        return "".join(result)

    def decompress(self, compressed):
        if not compressed:
            return ""
        result = []
        count_str = []
        for char in compressed:
            if char.isdigit():
                count_str.append(char)
            else:
                count = int("".join(count_str))
                result.append(char * count)
                count_str = []
        return "".join(result)

if __name__ == '__main__':
    encoder = RunLengthEncoder()
    original = "aaabbcccc"
    compressed = encoder.compress(original)
    print(compressed)
    decompressed = encoder.decompress(compressed)
    print(decompressed)
    empty_original = ""
    empty_compressed = encoder.compress(empty_original)
    print(empty_compressed)
    empty_decompressed = encoder.decompress(empty_compressed)
    print(empty_decompressed)