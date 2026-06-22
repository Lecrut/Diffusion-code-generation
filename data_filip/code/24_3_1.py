import threading

class RLECodec:
    def __init__(self):
        self._lock = threading.Lock()
        self.sample_data = "AAAABBBCCDAA"

    def compress(self, data):
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

    def decompress(self, data):
        with self._lock:
            if not data:
                return ""
            decompressed = []
            i = 0
            while i < len(data):
                if not data[i].isdigit():
                    raise ValueError("Invalid RLE string format")
                count_str = ""
                while i < len(data) and data[i].isdigit():
                    count_str += data[i]
                    i += 1
                if i >= len(data):
                    raise ValueError("Invalid RLE string format")
                count = int(count_str)
                char = data[i]
                decompressed.append(char * count)
                i += 1
            return "".join(decompressed)

if __name__ == '__main__':
    codec = RLECodec()
    original = codec.sample_data
    compressed = codec.compress(original)
    decompressed = codec.decompress(compressed)
    print(compressed)
    print(decompressed)