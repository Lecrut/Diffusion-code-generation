class RunLengthEncoder:
    def __init__(self):
        self.compression_mode = "count-char"

    def compress(self, text: str) -> str:
        if not text:
            return ""
        result = []
        index = 0
        length = len(text)
        while index < length:
            current_char = text[index]
            count = 1
            while index + 1 < length and text[index + 1] == current_char:
                count += 1
                index += 1
            result.append(str(count))
            result.append(current_char)
            index += 1
        return "".join(result)

    def decompress(self, encoded: str) -> str:
        if not encoded:
            return ""
        result = []
        index = 0
        length = len(encoded)
        while index < length:
            count_str = ""
            while index < length and encoded[index].isdigit():
                count_str += encoded[index]
                index += 1
            if index >= length:
                break
            char = encoded[index]
            count = int(count_str)
            result.append(char * count)
            index += 1
        return "".join(result)

if __name__ == "__main__":
    encoder = RunLengthEncoder()
    test_string_1 = "AAABBBCCCCDDDEEEEEFFFFGG"
    compressed_1 = encoder.compress(test_string_1)
    print(compressed_1)
    decompressed_1 = encoder.decompress(compressed_1)
    print(decompressed_1)
    
    test_string_2 = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW"
    compressed_2 = encoder.compress(test_string_2)
    print(compressed_2)
    decompressed_2 = encoder.decompress(compressed_2)
    print(decompressed_2)
    
    test_string_3 = "A"
    compressed_3 = encoder.compress(test_string_3)
    print(compressed_3)
    decompressed_3 = encoder.decompress(compressed_3)
    print(decompressed_3)
    
    test_string_4 = ""
    compressed_4 = encoder.compress(test_string_4)
    print(compressed_4)
    decompressed_4 = encoder.decompress(compressed_4)
    print(decompressed_4)
    
    test_string_5 = "12345"
    compressed_5 = encoder.compress(test_string_5)
    print(compressed_5)
    decompressed_5 = encoder.decompress(compressed_5)
    print(decompressed_5)