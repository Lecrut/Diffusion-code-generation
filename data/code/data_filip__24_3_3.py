import threading

class RLECodec:
    def __init__(self):
        self.lock = threading.Lock()
        self.sample_data = "aaabbbcccaaa"
        self.compressed_cache = None

    def compress(self, data):
        with self.lock:
            if not data:
                return ""
            result = []
            count = 1
            for i in range(1, len(data)):
                if data[i] == data[i - 1]:
                    count += 1
                else:
                    result.append(f"{data[i - 1]}{count}")
                    count = 1
            result.append(f"{data[-1]}{count}")
            self.compressed_cache = "".join(result)
            return self.compressed_cache

    def decompress(self, data):
        with self.lock:
            if not data:
                return ""
            result = []
            count_str = ""
            for char in data:
                if char.isdigit():
                    count_str += char
                else:
                    count = int(count_str) if count_str else 1
                    result.append(char * count)
                    count_str = ""
            return "".join(result)

    def get_sample_compression(self):
        return self.compress(self.sample_data)

    def get_sample_decompression(self):
        original = self.decompress(self.get_sample_compression())
        return original

if __name__ == '__main__':
    codec = RLECodec()
    compressed = codec.get_sample_compression()
    decompressed = codec.get_sample_decompression()
    print(compressed)
    print(decompressed)