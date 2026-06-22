class RunLengthEncoder:
    def __init__(self, count_threshold=2):
        self.count_threshold = count_threshold

    def _handle_empty_input(self, data):
        return "" if isinstance(data, str) else b""

    def _compress_string(self, text):
        if not text:
            return ""
        result = []
        current_char = text[0]
        count = 1
        for i in range(1, len(text)):
            if text[i] == current_char:
                count += 1
            else:
                if count >= self.count_threshold:
                    result.append(f"{count}{current_char}")
                else:
                    result.append(current_char * count)
                current_char = text[i]
                count = 1
        if count >= self.count_threshold:
            result.append(f"{count}{current_char}")
        else:
            result.append(current_char * count)
        return "".join(result)

    def compress(self, data):
        if not isinstance(data, str):
            return self._handle_empty_input(data)
        return self._compress_string(data)

    def _decompress_string(self, text):
        if not text:
            return ""
        result = []
        i = 0
        while i < len(text):
            if text[i].isdigit():
                count_str = ""
                while i < len(text) and text[i].isdigit():
                    count_str += text[i]
                    i += 1
                count = int(count_str)
                if i < len(text):
                    char = text[i]
                    result.append(char * count)
                    i += 1
                else:
                    i += 1
            else:
                result.append(text[i])
                i += 1
        return "".join(result)

    def decompress(self, data):
        if not isinstance(data, str):
            return self._handle_empty_input(data)
        return self._decompress_string(data)

if __name__ == '__main__':
    encoder = RunLengthEncoder(count_threshold=3)
    original_text = "AAABBBCCDAAAA"
    compressed_text = encoder.compress(original_text)
    decompressed_text = encoder.decompress(compressed_text)
    print(f"Original: {original_text}")
    print(f"Compressed: {compressed_text}")
    print(f"Decompressed: {decompressed_text}")
    
    test_cases = [
        "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW",
        "AAAAAABBBBBCCCCDD",
        "ABC",
        "",
        "A",
        "AA"
    ]
    
    for test in test_cases:
        c = encoder.compress(test)
        d = encoder.decompress(c)
        status = "OK" if d == test else "FAIL"
        print(f"{status}: {test} -> {c} -> {d}")