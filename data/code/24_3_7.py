import threading

class RLECodec:
    def __init__(self):
        self._lock = threading.Lock()
        self.sample_data = {
            "compressed": "aaabbcdddd",
            "expected_rle": "3a2b1c4d"
        }

    def compress(self, data):
        if not data:
            return ""
        
        result = []
        count = 1
        current_char = data[0]
        
        for i in range(1, len(data)):
            if data[i] == current_char:
                count += 1
            else:
                result.append(f"{count}{current_char}")
                current_char = data[i]
                count = 1
        
        result.append(f"{count}{current_char}")
        return "".join(result)

    def decompress(self, rle_data):
        if not rle_data:
            return ""
        
        result = []
        count = 0
        i = 0
        
        while i < len(rle_data):
            char = rle_data[i]
            if char.isdigit():
                count = count * 10 + int(char)
            else:
                if count == 0:
                    count = 1
                result.append(char * count)
                count = 0
            i += 1
        
        return "".join(result)

    def run_tests(self):
        with self._lock:
            input_str = self.sample_data["compressed"]
            expected = self.sample_data["expected_rle"]
            
            compressed = self.compress(input_str)
            decompressed = self.decompress(compressed)
            
            return {
                "original": input_str,
                "compressed": compressed,
                "expected_compression": expected,
                "decompressed": decompressed,
                "round_trip_success": input_str == decompressed and compressed == expected
            }

if __name__ == '__main__':
    codec = RLECodec()
    results = codec.run_tests()
    print(f"Original: {results['original']}")
    print(f"Compressed: {results['compressed']}")
    print(f"Expected Compressed: {results['expected_compression']}")
    print(f"Decompressed: {results['decompressed']}")
    print(f"Round Trip Success: {results['round_trip_success']}")