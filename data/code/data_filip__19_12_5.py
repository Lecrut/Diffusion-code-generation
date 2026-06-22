import os

class RLECompressor:
    def __init__(self, text):
        self.text = text
        self.compressed = self.compress()
        self.decompressed = self.decompress(self.compressed)

    def compress(self):
        if not self.text:
            return ""
        compressed = []
        current_char = self.text[0]
        count = 1
        for char in self.text[1:]:
            if char == current_char:
                count += 1
            else:
                compressed.append(str(count) + current_char)
                current_char = char
                count = 1
        compressed.append(str(count) + current_char)
        return "".join(compressed)

    def decompress(self, compressed_str):
        if not compressed_str:
            return ""
        decompressed = []
        i = 0
        while i < len(compressed_str):
            count_str = ""
            while i < len(compressed_str) and compressed_str[i].isdigit():
                count_str += compressed_str[i]
                i += 1
            if i < len(compressed_str):
                char = compressed_str[i]
                i += 1
                decompressed.append(char * int(count_str))
        return "".join(decompressed)

    def get_compression_ratio(self):
        if len(self.text) == 0:
            return 0
        return len(self.compressed) / len(self.text)

if __name__ == '__main__':
    sample_text = "AAAABBBCCDAA"
    compressor = RLECompressor(sample_text)
    print(compressor.compressed)
    print(compressor.decompressed)
    print(compressor.get_compression_ratio())