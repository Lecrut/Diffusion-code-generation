class RunLengthEncoder:
    def __init__(self):
        self.buffer = []
        self.last_char = None
        self.count = 0

    def compress(self, text):
        if not text:
            return ""
        self.buffer = []
        self.last_char = text[0]
        self.count = 1
        for index in range(1, len(text)):
            current_char = text[index]
            if current_char == self.last_char:
                self.count += 1
            else:
                self._flush_buffer()
                self.last_char = current_char
                self.count = 1
        self._flush_buffer()
        return "".join(self.buffer)

    def _flush_buffer(self):
        self.buffer.append(str(self.count))
        self.buffer.append(self.last_char)

    def decompress(self, encoded):
        if not encoded:
            return ""
        result = []
        index = 0
        length = len(encoded)
        while index < length:
            num_str = ""
            while index < length and encoded[index].isdigit():
                num_str += encoded[index]
                index += 1
            if index >= length:
                break
            char = encoded[index]
            index += 1
            try:
                count = int(num_str)
            except ValueError:
                count = 1
            result.append(char * count)
        return "".join(result)

if __name__ == '__main__':
    encoder = RunLengthEncoder()
    test_string_a = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW"
    compressed_a = encoder.compress(test_string_a)
    decompressed_a = encoder.decompress(compressed_a)
    print(f"Original: {test_string_a}")
    print(f"Compressed: {compressed_a}")
    print(f"Decompressed: {decompressed_a}")
    print(f"Round-trip match: {test_string_a == decompressed_a}")
    
    test_string_b = "aaabbbaacccdddd"
    compressed_b = encoder.compress(test_string_b)
    decompressed_b = encoder.decompress(compressed_b)
    print(f"Original: {test_string_b}")
    print(f"Compressed: {compressed_b}")
    print(f"Decompressed: {decompressed_b}")
    print(f"Round-trip match: {test_string_b == decompressed_b}")
    
    test_string_c = ""
    compressed_c = encoder.compress(test_string_c)
    decompressed_c = encoder.decompress(compressed_c)
    print(f"Empty test match: {test_string_c == decompressed_c}")