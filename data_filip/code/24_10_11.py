class RunLengthEncoder:
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
                result.append(str(count) + current_char)
                current_char = data[i]
                count = 1
        result.append(str(count) + current_char)
        return "".join(result)

    def decompress(self, data):
        if not data:
            return ""
        result = []
        i = 0
        while i < len(data):
            count_str = ""
            while i < len(data) and data[i].isdigit():
                count_str += data[i]
                i += 1
            count = int(count_str)
            if i < len(data):
                char = data[i]
                result.append(char * count)
                i += 1
        return "".join(result)

if __name__ == "__main__":
    encoder = RunLengthEncoder()
    test_string_1 = "AAAABBBCCDA"
    compressed_1 = encoder.compress(test_string_1)
    decompressed_1 = encoder.decompress(compressed_1)
    print(f"Original: {test_string_1}")
    print(f"Compressed: {compressed_1}")
    print(f"Decompressed: {decompressed_1}")
    test_string_2 = "WWWWWWWWWWWWBWWWWWWWWWWWWBBB"
    compressed_2 = encoder.compress(test_string_2)
    decompressed_2 = encoder.decompress(compressed_2)
    print(f"Original: {test_string_2}")
    print(f"Compressed: {compressed_2}")
    print(f"Decompressed: {decompressed_2}")