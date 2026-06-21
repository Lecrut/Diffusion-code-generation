import threading

class RLECodec:
    def __init__(self):
        self._lock = threading.Lock()
        self._sample_data = "aaabbccccd"

    def compress(self, text):
        if not text:
            return ""
        compressed = []
        current_char = text[0]
        count = 1
        for char in text[1:]:
            if char == current_char:
                count += 1
            else:
                compressed.append(f"{current_char}{count}")
                current_char = char
                count = 1
        compressed.append(f"{current_char}{count}")
        return "".join(compressed)

    def decompress(self, text):
        if not text:
            return ""
        decompressed = []
        i = 0
        while i < len(text):
            char = text[i]
            i += 1
            count_str = ""
            while i < len(text) and text[i].isdigit():
                count_str += text[i]
                i += 1
            count = int(count_str)
            decompressed.append(char * count)
        return "".join(decompressed)

    def run_test(self):
        with self._lock:
            original = self._sample_data
            compressed = self.compress(original)
            restored = self.decompress(compressed)
            return original, compressed, restored

if __name__ == "__main__":
    codec = RLECodec()
    result = codec.run_test()
    print(f"Original: {result[0]}")
    print(f"Compressed: {result[1]}")
    print(f"Restored: {result[2]}")