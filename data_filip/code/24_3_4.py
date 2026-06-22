import threading
import re

class RLECodec:
    def __init__(self, sample_data):
        self.sample_data = sample_data
        self._lock = threading.Lock()

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
                    compressed.append(f"{count}{current_char}")
                    current_char = char
                    count = 1
            compressed.append(f"{count}{current_char}")
            return "".join(compressed)

    def decompress(self, compressed_text):
        with self._lock:
            if not compressed_text:
                return ""
            decompressed = []
            pattern = re.compile(r'(\d+)(\D)')
            matches = pattern.findall(compressed_text)
            for count_str, char in matches:
                count = int(count_str)
                decompressed.append(char * count)
            return "".join(decompressed)

if __name__ == '__main__':
    sample_string = "AAAABBBCCDAA"
    codec = RLECodec(sample_string)
    compressed = codec.compress(sample_string)
    print(compressed)
    decompressed = codec.decompress(compressed)
    print(decompressed)