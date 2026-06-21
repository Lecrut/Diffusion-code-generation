import threading

class RLECodec:
    def __init__(self):
        self._lock = threading.Lock()
        self._samples = {
            'input': "AAABBBCCD",
            'compressed': "A3B3C2D",
            'decompressed': "AAABBBCCD",
        }

    def compress(self, data):
        with self._lock:
            if not data:
                return ""
            result = []
            count = 1
            for i in range(1, len(data)):
                if data[i] == data[i - 1]:
                    count += 1
                else:
                    result.append(data[i - 1] + str(count))
                    count = 1
            result.append(data[-1] + str(count))
            return "".join(result)

    def decompress(self, data):
        with self._lock:
            if not data:
                return ""
            result = []
            i = 0
            while i < len(data):
                char = data[i]
                i += 1
                num_str = ""
                while i < len(data) and data[i].isdigit():
                    num_str += data[i]
                    i += 1
                if num_str:
                    result.append(char * int(num_str))
                else:
                    result.append(char)
            return "".join(result)

if __name__ == '__main__':
    codec = RLECodec()
    original = codec._samples['input']
    compressed = codec.compress(original)
    decompressed = codec.decompress(compressed)
    print(f"Original: {original}")
    print(f"Compressed: {compressed}")
    print(f"Decompressed: {decompressed}")