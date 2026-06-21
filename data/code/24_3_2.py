import threading

class RLECodec:
    def __init__(self):
        self._lock = threading.Lock()
        self._cache = {}

    def compress(self, text: str) -> str:
        with self._lock:
            if text in self._cache:
                return self._cache[text]
            if not text:
                return ""
            compressed = []
            current_char = text[0]
            count = 1
            for char in text[1:]:
                if char == current_char:
                    count += 1
                else:
                    compressed.append(f"{count}{current_char}")
                    current_char = char
                    count = 1
            compressed.append(f"{count}{current_char}")
            result = "".join(compressed)
            self._cache[text] = result
            return result

    def decompress(self, compressed: str) -> str:
        with self._lock:
            if not compressed:
                return ""
            result = []
            i = 0
            length = len(compressed)
            while i < length:
                count_str = []
                while i < length and compressed[i].isdigit():
                    count_str.append(compressed[i])
                    i += 1
                count = int("".join(count_str)) if count_str else 1
                if i < length:
                    char = compressed[i]
                    i += 1
                    result.append(char * count)
                else:
                    raise ValueError("Invalid compressed string: count without character.")
            return "".join(result)

if __name__ == '__main__':
    codec = RLECodec()
    original = "AAABBBCCDAA"
    compressed = codec.compress(original)
    decompressed = codec.decompress(compressed)
    print(f"Original: {original}")
    print(f"Compressed: {compressed}")
    print(f"Decompressed: {decompressed}")
    print(f"Match: {original == decompressed}")