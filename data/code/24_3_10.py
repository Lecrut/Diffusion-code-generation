import threading

class RLECodec:
    def __init__(self):
        self._lock = threading.RLock()
        self.sample_input = "AAAABBBCCDAA"

    def compress(self, data):
        if not data:
            return ""
        with self._lock:
            if len(data) == 0:
                return ""
            compressed = []
            count = 1
            current_char = data[0]
            for i in range(1, len(data)):
                if data[i] == current_char:
                    count += 1
                else:
                    compressed.append(f"{count}{current_char}")
                    current_char = data[i]
                    count = 1
            compressed.append(f"{count}{current_char}")
            return "".join(compressed)

    def decompress(self, data):
        if not data:
            return ""
        with self._lock:
            if len(data) == 0:
                return ""
            decompressed = []
            i = 0
            while i < len(data):
                count_str = ""
                while i < len(data) and data[i].isdigit():
                    count_str += data[i]
                    i += 1
                if i >= len(data):
                    break
                char = data[i]
                count = int(count_str) if count_str else 1
                decompressed.append(char * count)
                i += 1
            return "".join(decompressed)

    def get_sample_input(self):
        with self._lock:
            return self.sample_input

if __name__ == '__main__':
    codec = RLECodec()
    sample = codec.get_sample_input()
    compressed = codec.compress(sample)
    decompressed = codec.decompress(compressed)
    print(compressed)
    print(decompressed)