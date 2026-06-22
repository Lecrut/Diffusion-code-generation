class RunLengthEncoder:
    def encode(self, text):
        if not text:
            return ""
        result = []
        count = 1
        for i in range(1, len(text)):
            if text[i] == text[i - 1]:
                count += 1
            else:
                result.append(f"{count}{text[i - 1]}")
                count = 1
        result.append(f"{count}{text[-1]}")
        return "".join(result)

    def decode(self, encoded_text):
        if not encoded_text:
            return ""
        result = []
        i = 0
        while i < len(encoded_text):
            num_str = ""
            while i < len(encoded_text) and encoded_text[i].isdigit():
                num_str += encoded_text[i]
                i += 1
            if i < len(encoded_text):
                char = encoded_text[i]
                count = int(num_str)
                result.append(char * count)
                i += 1
        return "".join(result)

if __name__ == '__main__':
    encoder = RunLengthEncoder()
    test_string = "AAABBBCCCCDDDDDD"
    compressed = encoder.encode(test_string)
    decompressed = encoder.decode(compressed)
    print(compressed)
    print(decompressed)
    test_string_two = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB"
    compressed_two = encoder.encode(test_string_two)
    decompressed_two = encoder.decode(compressed_two)
    print(compressed_two)
    print(decompressed_two)