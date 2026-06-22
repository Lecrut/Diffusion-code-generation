class RunLengthEncoder:
    def compress(self, data):
        if not data:
            return ""
        compressed = []
        current_char = data[0]
        count = 1
        for i in range(1, len(data)):
            if data[i] == current_char:
                count += 1
            else:
                compressed.append(str(count) + current_char)
                current_char = data[i]
                count = 1
        compressed.append(str(count) + current_char)
        return "".join(compressed)

    def decompress(self, data):
        if not data:
            return ""
        decompressed = []
        i = 0
        while i < len(data):
            count = ""
            while i < len(data) and data[i].isdigit():
                count += data[i]
                i += 1
            if i < len(data):
                char = data[i]
                decompressed.append(char * int(count))
                i += 1
        return "".join(decompressed)

if __name__ == '__main__':
    encoder = RunLengthEncoder()
    test_string = "AAAABBBCCDAA"
    compressed = encoder.compress(test_string)
    decompressed = encoder.decompress(compressed)
    print(compressed)
    print(decompressed)
    test_string_two = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB"
    compressed_two = encoder.compress(test_string_two)
    decompressed_two = encoder.decompress(compressed_two)
    print(compressed_two)
    print(decompressed_two)
    test_string_three = ""
    compressed_three = encoder.compress(test_string_three)
    decompressed_three = encoder.decompress(compressed_three)
    print(compressed_three)
    print(decompressed_three)