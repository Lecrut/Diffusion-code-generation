import threading

class RLECodec:
    def __init__(self):
        self._lock = threading.RLock()
        self._sample_data = {
            "aabcccccaaa": "2a1b5c3a",
            "hello   world": "1h1e2l1o6 1w1o1r1l1d"
        }

    def _run(self, func, *args):
        with self._lock:
            return func(*args)

    def compress(self, data):
        if not data:
            return ""
        return self._run(self._encode, data)

    def decompress(self, data):
        if not data:
            return ""
        return self._run(self._decode, data)

    def _encode(self, data):
        if len(data) == 0:
            return ""
        compressed = []
        current_char = data[0]
        count = 1
        for i in range(1, len(data)):
            if data[i] == current_char:
                count += 1
            else:
                compressed.append(str(count))
                compressed.append(current_char)
                current_char = data[i]
                count = 1
        compressed.append(str(count))
        compressed.append(current_char)
        return "".join(compressed)

    def _decode(self, data):
        if len(data) == 0:
            return ""
        decompressed = []
        i = 0
        while i < len(data):
            count_str = ""
            while i < len(data) and data[i].isdigit():
                count_str += data[i]
                i += 1
            if i < len(data):
                count = int(count_str)
                char = data[i]
                decompressed.append(char * count)
                i += 1
            else:
                break
        return "".join(decompressed)

    def get_sample_test_result(self):
        original = self._sample_data["aabcccccaaa"]
        compressed = self.compress(original)
        decompressed = self.decompress(compressed)
        return compressed, decompressed

if __name__ == '__main__':
    codec = RLECodec()
    test_input = "aaabbccccdddd"
    encoded = codec.compress(test_input)
    decoded = codec.decompress(encoded)
    print(encoded)
    print(decoded)
    sample_result = codec.get_sample_test_result()
    print(sample_result)