import threading

class RLECodec:
    def __init__(self):
        self.lock = threading.Lock()
        self.sample_data = "AAABBBDDDDCCCCAAAEFFFGHHHJJJKKKLL"

    def compress(self, text):
        if not text:
            return ""
        with self.lock:
            compressed = []
            current_char = text[0]
            count = 1
            for char in text[1:]:
                if char == current_char:
                    count += 1
                else:
                    compressed.append(f"{count}{current_char}")
                    current_char = char
                    count = 1
            compressed.append(f"{count}{current_char}")
            return "".join(compressed)

    def decompress(self, compressed):
        if not compressed:
            return ""
        with self.lock:
            decompressed = []
            i = 0
            while i < len(compressed):
                if not compressed[i].isdigit():
                    decompressed.append(compressed[i])
                    i += 1
                else:
                    count_str = ""
                    while i < len(compressed) and compressed[i].isdigit():
                        count_str += compressed[i]
                        i += 1
                    if i < len(compressed):
                        count = int(count_str)
                        char = compressed[i]
                        decompressed.append(char * count)
                        i += 1
                    else:
                        raise ValueError("Invalid compressed string")
            return "".join(decompressed)

if __name__ == '__main__':
    codec = RLECodec()
    original = codec.sample_data
    compressed = codec.compress(original)
    decompressed = codec.decompress(compressed)
    print(f"Original: {original}")
    print(f"Compressed: {compressed}")
    print(f"Decompressed: {decompressed}")
    print(f"Match: {original == decompressed}")