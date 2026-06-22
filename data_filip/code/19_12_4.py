def rle_compress(data):
    if not data:
        return ""
    compressed = []
    current_char = data[0]
    count = 1
    for char in data[1:]:
        if char == current_char and count < 9:
            count += 1
        else:
            compressed.append(str(count) + current_char)
            current_char = char
            count = 1
    compressed.append(str(count) + current_char)
    return "".join(compressed)

def rle_decompress(data):
    if not data:
        return ""
    decompressed = []
    i = 0
    while i < len(data):
        count = int(data[i])
        char = data[i + 1]
        decompressed.append(char * count)
        i += 2
    return "".join(decompressed)

class RLEProcessor:
    def __init__(self, text):
        self.text = text

    def compress(self):
        return rle_compress(self.text)

    def decompress(self, compressed_data):
        return rle_decompress(compressed_data)

if __name__ == '__main__':
    sample_text = "AAABBBCCD"
    processor = RLEProcessor(sample_text)
    compressed = processor.compress()
    print(compressed)
    decompressed = processor.decompress(compressed)
    print(decompressed)