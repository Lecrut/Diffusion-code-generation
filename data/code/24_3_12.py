import threading

class RLECodec:
    def __init__(self):
        self._lock = threading.Lock()
        self._sample_data = "aaabbbccccdddeeefff"

    def _compress_segment(self, text):
        if not text:
            return ""
        result = []
        count = 1
        for i in range(1, len(text)):
            if text[i] == text[i - 1]:
                count += 1
            else:
                result.append(f"{count}{text[i - 1]}")
                count = 1
        result.append(f"{count}{text[-1]}")
        return "".join(result)

    def _decompress_segment(self, text):
        if not text:
            return ""
        result = []
        i = 0
        while i < len(text):
            num_str = ""
            while i < len(text) and text[i].isdigit():
                num_str += text[i]
                i += 1
            if i < len(text):
                char = text[i]
                i += 1
                count = int(num_str) if num_str else 1
                result.append(char * count)
        return "".join(result)

    def compress(self, text):
        with self._lock:
            if text == self._sample_data:
                return self._compress_segment(text)
            return self._compress_segment(text)

    def decompress(self, text):
        with self._lock:
            return self._decompress_segment(text)

    def get_sample_data(self):
        with self._lock:
            return self._sample_data

if __name__ == '__main__':
    codec = RLECodec()
    original = codec.get_sample_data()
    compressed = codec.compress(original)
    decompressed = codec.decompress(compressed)
    print(f"Original: {original}")
    print(f"Compressed: {compressed}")
    print(f"Decompressed: {decompressed}")
    print(f"Match: {original == decompressed}")