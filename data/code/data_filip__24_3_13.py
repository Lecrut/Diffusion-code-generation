import threading

class RLECodec:
    def __init__(self):
        self._lock = threading.Lock()
        self.sample_data = [
            ("AAABBBCCCC", "3A3B4C"),
            ("WWWWWWWWWWWWBWWWWWWWWWWWWBBB", "12W1B12W3B"),
            ("", ""),
            ("A", "1A"),
            ("ABB", "1A2B")
        ]

    def compress(self, data):
        with self._lock:
            if not data:
                return ""
            result = []
            count = 1
            for i in range(1, len(data)):
                if data[i] == data[i-1]:
                    count += 1
                else:
                    result.append(str(count))
                    result.append(data[i-1])
                    count = 1
            result.append(str(count))
            result.append(data[-1])
            return "".join(result)

    def decompress(self, data):
        with self._lock:
            if not data:
                return ""
            result = []
            i = 0
            while i < len(data):
                num_start = i
                while i < len(data) and data[i].isdigit():
                    i += 1
                if i == num_start:
                    raise ValueError("Invalid RLE format")
                count = int(data[num_start:i])
                if i >= len(data):
                    raise ValueError("Invalid RLE format: missing character")
                char = data[i]
                result.append(char * count)
                i += 1
            return "".join(result)

if __name__ == '__main__':
    codec = RLECodec()
    for original, expected_compressed in codec.sample_data:
        compressed = codec.compress(original)
        decompressed = codec.decompress(compressed)
        print(f"Original: {original}")
        print(f"Compressed: {compressed}")
        print(f"Decompressed: {decompressed}")
        print("-" * 20)