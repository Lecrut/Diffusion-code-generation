import threading

class RLECodec:
    def __init__(self):
        self._lock = threading.Lock()
        self._sample_data = "AAABBBCCCDDD"

    def compress(self, text):
        with self._lock:
            if not text:
                return ""
            compressed = []
            current_char = text[0]
            count = 1
            for char in text[1:]:
                if char == current_char:
                    count += 1
                else:
                    compressed.append(f"{current_char}{count}")
                    current_char = char
                    count = 1
            compressed.append(f"{current_char}{count}")
            return "".join(compressed)

    def decompress(self, compressed_text):
        with self._lock:
            if not compressed_text:
                return ""
            decompressed = []
            i = 0
            while i < len(compressed_text):
                char = compressed_text[i]
                i += 1
                num_str = ""
                while i < len(compressed_text) and compressed_text[i].isdigit():
                    num_str += compressed_text[i]
                    i += 1
                count = int(num_str) if num_str else 1
                decompressed.append(char * count)
            return "".join(decompressed)

if __name__ == '__main__':
    codec = RLECodec()
    original = codec._sample_data
    compressed = codec.compress(original)
    decompressed = codec.decompress(compressed)
    print(f"Original: {original}")
    print(f"Compressed: {compressed}")
    print(f"Decompressed: {decompressed}")
    print(codec.compress(""))
    print(codec.decompress(""))