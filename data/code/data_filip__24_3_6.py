import threading
from typing import List, Tuple

class RLECodec:
    def __init__(self):
        self._lock = threading.Lock()
        self._sample_data = "AAAABBBCCDAA"

    def compress(self, data: str) -> str:
        with self._lock:
            if not data:
                return ""
            compressed = []
            current_char = data[0]
            count = 1
            for char in data[1:]:
                if char == current_char:
                    count += 1
                else:
                    compressed.append(f"{count}{current_char}")
                    current_char = char
                    count = 1
            compressed.append(f"{count}{current_char}")
            return "".join(compressed)

    def decompress(self, compressed_data: str) -> str:
        with self._lock:
            if not compressed_data:
                return ""
            decompressed = []
            i = 0
            while i < len(compressed_data):
                if not compressed_data[i].isdigit():
                    raise ValueError(f"Invalid compressed data at index {i}: expected digit")
                count_str = ""
                while i < len(compressed_data) and compressed_data[i].isdigit():
                    count_str += compressed_data[i]
                    i += 1
                count = int(count_str)
                if i >= len(compressed_data):
                    raise ValueError("Invalid compressed data: missing character after count")
                char = compressed_data[i]
                decompressed.append(char * count)
                i += 1
            return "".join(decompressed)

if __name__ == '__main__':
    codec = RLECodec()
    sample = codec._sample_data
    compressed = codec.compress(sample)
    decompressed = codec.decompress(compressed)
    print(f"Original: {sample}")
    print(f"Compressed: {compressed}")
    print(f"Decompressed: {decompressed}")
    print(f"Match: {sample == decompressed}")