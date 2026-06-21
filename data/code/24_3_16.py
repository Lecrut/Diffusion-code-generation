import threading
import re

class RLECodec:
    def __init__(self):
        self._lock = threading.Lock()
        self._sample_data = [
            "aaabbc",
            "wwwwwwwwwwwwwwwwwwwww",
            "hello",
            "1122334455",
            "!!@@##$$%%^^&&**(()"
        ]

    def compress(self, data):
        if not data:
            return ""
        
        result = []
        count = 1
        for i in range(len(data)):
            if i + 1 < len(data) and data[i] == data[i + 1]:
                count += 1
            else:
                if count > 1:
                    result.append(f"{count}{data[i]}")
                else:
                    result.append(data[i])
                count = 1
        return "".join(result)

    def decompress(self, data):
        if not data:
            return ""
        
        result = []
        i = 0
        while i < len(data):
            if data[i].isdigit():
                j = i
                while j < len(data) and data[j].isdigit():
                    j += 1
                count = int(data[i:j])
                if j < len(data):
                    result.append(data[j] * count)
                    i = j + 1
                else:
                    i = j
            else:
                result.append(data[i])
                i += 1
        return "".join(result)

    def test_roundtrip(self):
        results = []
        with self._lock:
            for sample in self._sample_data:
                compressed = self.compress(sample)
                decompressed = self.decompress(compressed)
                results.append({
                    "original": sample,
                    "compressed": compressed,
                    "decompressed": decompressed,
                    "match": sample == decompressed
                })
        return results

if __name__ == '__main__':
    codec = RLECodec()
    test_results = codec.test_roundtrip()
    for item in test_results:
        print(f"Original: {item['original']}")
        print(f"Compressed: {item['compressed']}")
        print(f"Decompressed: {item['decompressed']}")
        print(f"Match: {item['match']}")
        print("-" * 30)