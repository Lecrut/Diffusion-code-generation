import threading

class RLECodec:
    def __init__(self):
        self._lock = threading.Lock()
        self._sample_data = {
            "aaabbbcccc": "3a3b4c",
            "": "",
            "a": "1a",
            "aabb": "2a2b",
            "hello": "1h1e2l1o"
        }

    def _run_rle_compress(self, text):
        if not text:
            return ""
        result = []
        count = 1
        current_char = text[0]
        for i in range(1, len(text)):
            if text[i] == current_char:
                count += 1
            else:
                result.append(f"{count}{current_char}")
                current_char = text[i]
                count = 1
        result.append(f"{count}{current_char}")
        return "".join(result)

    def _run_rle_decompress(self, encoded):
        if not encoded:
            return ""
        result = []
        i = 0
        while i < len(encoded):
            if not encoded[i].isdigit():
                raise ValueError("Invalid encoded string")
            num_str = ""
            while i < len(encoded) and encoded[i].isdigit():
                num_str += encoded[i]
                i += 1
            if i >= len(encoded):
                raise ValueError("Invalid encoded string")
            count = int(num_str)
            char = encoded[i]
            result.append(char * count)
            i += 1
        return "".join(result)

    def compress(self, text):
        with self._lock:
            return self._run_rle_compress(text)

    def decompress(self, encoded):
        with self._lock:
            return self._run_rle_decompress(encoded)

if __name__ == '__main__':
    codec = RLECodec()
    sample_string = "aaabbbcccc"
    compressed = codec.compress(sample_string)
    decompressed = codec.decompress(compressed)
    print(f"Original: {sample_string}")
    print(f"Compressed: {compressed}")
    print(f"Decompressed: {decompressed}")
    
    for original, expected_compressed in codec._sample_data.items():
        if original:
            res = codec.compress(original)
            print(f"Compress('{original}') -> {res}")
        else:
            res = codec.compress(original)
            print(f"Compress('') -> '{res}'")
            
    for encoded, expected_original in codec._sample_data.items():
        if encoded:
            res = codec.decompress(encoded)
            print(f"Decompress('{encoded}') -> {res}")
        else:
            res = codec.decompress(encoded)
            print(f"Decompress('') -> '{res}'")