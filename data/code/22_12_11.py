class RLECompressor:
    def compress(self, s):
        if not s:
            return ""
        compressed = []
        count = 1
        current_char = s[0]
        for i in range(1, len(s)):
            if s[i] == current_char:
                count += 1
            else:
                compressed.append(f"{count}{current_char}")
                current_char = s[i]
                count = 1
        compressed.append(f"{count}{current_char}")
        return "".join(compressed)

    def decompress(self, s):
        if not s:
            return ""
        decompressed = []
        i = 0
        while i < len(s):
            num_str = ""
            while i < len(s) and s[i].isdigit():
                num_str += s[i]
                i += 1
            if not num_str:
                break
            if i < len(s):
                char = s[i]
                count = int(num_str)
                decompressed.append(char * count)
                i += 1
            else:
                break
        return "".join(decompressed)

if __name__ == '__main__':
    compressor = RLECompressor()
    original = "aaabbccccd"
    compressed = compressor.compress(original)
    decompressed = compressor.decompress(compressed)
    print(compressed)
    print(decompressed)