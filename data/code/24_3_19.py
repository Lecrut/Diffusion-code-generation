import threading

class RLECodec:
    def __init__(self):
        self._lock = threading.Lock()
        self._sample_data = "aaabbbccccdddddeeeee"

    def compress(self, data):
        if not data:
            return ""
        with self._lock:
            result = []
            count = 1
            length = len(data)
            for i in range(length):
                if i + 1 < length and data[i] == data[i + 1]:
                    count += 1
                else:
                    result.append(f"{data[i]}{count}")
                    count = 1
            return "".join(result)

    def decompress(self, data):
        if not data:
            return ""
        with self._lock:
            result = []
            i = 0
            length = len(data)
            while i < length:
                char = data[i]
                i += 1
                num_str = ""
                while i < length and data[i].isdigit():
                    num_str += data[i]
                    i += 1
                count = int(num_str)
                result.append(char * count)
            return "".join(result)

if __name__ == "__main__":
    codec = RLECodec()
    compressed = codec.compress(codec._sample_data)
    decompressed = codec.decompress(compressed)
    print(f"Original: {codec._sample_data}")
    print(f"Compressed: {compressed}")
    print(f"Decompressed: {decompressed}")