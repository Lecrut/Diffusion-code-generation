import threading

class RLECodec:
    def __init__(self):
        self._lock = threading.Lock()
        self._sample_data = "AAAABBBCCDAA"

    def compress(self, data):
        if not data:
            return ""
        with self._lock:
            result = []
            count = 1
            current_char = data[0]
            for i in range(1, len(data)):
                if data[i] == current_char:
                    count += 1
                else:
                    result.append(f"{count}{current_char}")
                    current_char = data[i]
                    count = 1
            result.append(f"{count}{current_char}")
            return "".join(result)

    def decompress(self, data):
        if not data:
            return ""
        with self._lock:
            result = []
            i = 0
            while i < len(data):
                count_str = ""
                while i < len(data) and data[i].isdigit():
                    count_str += data[i]
                    i += 1
                if i < len(data):
                    char = data[i]
                    count = int(count_str)
                    result.append(char * count)
                    i += 1
            return "".join(result)

if __name__ == "__main__":
    codec = RLECodec()
    original = codec._sample_data
    compressed = codec.compress(original)
    decompressed = codec.decompress(compressed)
    print(f"Original: {original}")
    print(f"Compressed: {compressed}")
    print(f"Decompressed: {decompressed}")
    print(f"Round-trip Match: {original == decompressed}")