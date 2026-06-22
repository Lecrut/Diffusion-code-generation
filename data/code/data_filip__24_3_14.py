import threading
from collections import defaultdict

class RLECodec:
    def __init__(self):
        self._lock = threading.Lock()
        self.sample_data = "AAABBBCCCCD"

    def compress(self, data):
        if not data:
            return ""
        with self._lock:
            result = []
            current_char = data[0]
            count = 1
            for char in data[1:]:
                if char == current_char:
                    count += 1
                else:
                    result.append(str(count) + current_char)
                    current_char = char
                    count = 1
            result.append(str(count) + current_char)
            return "".join(result)

    def decompress(self, data):
        if not data:
            return ""
        with self._lock:
            result = []
            i = 0
            while i < len(data):
                if not data[i].isdigit():
                    raise ValueError("Invalid compressed string format")
                count_str = ""
                while i < len(data) and data[i].isdigit():
                    count_str += data[i]
                    i += 1
                if i >= len(data):
                    raise ValueError("Invalid compressed string format")
                count = int(count_str)
                char = data[i]
                result.append(char * count)
                i += 1
            return "".join(result)

if __name__ == '__main__':
    codec = RLECodec()
    original = codec.sample_data
    compressed = codec.compress(original)
    decompressed = codec.decompress(compressed)
    print(original)
    print(compressed)
    print(decompressed)
    print(original == decompressed)