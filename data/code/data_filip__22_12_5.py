class RLECompressor:
    def compress(self, data):
        if not data:
            return ""
        result = []
        current_char = data[0]
        count = 1
        for i in range(1, len(data)):
            if data[i] == current_char:
                count += 1
            else:
                result.append(str(count) + current_char)
                current_char = data[i]
                count = 1
        result.append(str(count) + current_char)
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
                char = data[i]
                result.append(char * count)
                i += 1
        return "".join(result)

if __name__ == '__main__':
    compressor = RLECompressor()
    original = "aaabbbccccddee"
    compressed = compressor.compress(original)
    decompressed = compressor.decompress(compressed)
    print(compressed)
    print(decompressed)