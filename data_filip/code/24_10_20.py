class RunLengthEncoding:
    def compress(self, input_string):
        if not input_string:
            return ""
        result = []
        count = 1
        current_char = input_string[0]
        for i in range(1, len(input_string)):
            if input_string[i] == current_char:
                count += 1
            else:
                result.append(f"{count}{current_char}")
                current_char = input_string[i]
                count = 1
        result.append(f"{count}{current_char}")
        return "".join(result)

    def decompress(self, compressed_string):
        if not compressed_string:
            return ""
        result = []
        i = 0
        while i < len(compressed_string):
            count_str = []
            while i < len(compressed_string) and compressed_string[i].isdigit():
                count_str.append(compressed_string[i])
                i += 1
            count = int("".join(count_str))
            char = compressed_string[i]
            result.append(char * count)
            i += 1
        return "".join(result)

if __name__ == '__main__':
    encoder = RunLengthEncoding()
    test_string = "AAABBBCCCA"
    compressed = encoder.compress(test_string)
    decompressed = encoder.decompress(compressed)
    print(compressed)
    print(decompressed)