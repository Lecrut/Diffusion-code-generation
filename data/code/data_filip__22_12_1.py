class RLECompressor:
    def compress(self, text):
        if not isinstance(text, str):
            return ""
        if len(text) == 0:
            return ""
        compressed = []
        count = 1
        for i in range(1, len(text)):
            if text[i] == text[i - 1]:
                count += 1
            else:
                compressed.append(text[i - 1] + str(count) if count > 1 else text[i - 1])
                count = 1
        compressed.append(text[-1] + str(count) if count > 1 else text[-1])
        return "".join(compressed)

    def decompress(self, text):
        if not isinstance(text, str):
            return ""
        if len(text) == 0:
            return ""
        result = []
        i = 0
        while i < len(text):
            char = text[i]
            i += 1
            num_str = ""
            while i < len(text) and text[i].isdigit():
                num_str += text[i]
                i += 1
            if num_str:
                result.append(char * int(num_str))
            else:
                result.append(char)
        return "".join(result)

if __name__ == '__main__':
    compressor = RLECompressor()
    original = "AAABBBCCCCD"
    compressed = compressor.compress(original)
    decompressed = compressor.decompress(compressed)
    print(compressed)
    print(decompressed)
    print(compressor.compress("A"))
    print(compressor.decompress("A5"))
    print(compressor.compress(""))
    print(compressor.decompress(""))