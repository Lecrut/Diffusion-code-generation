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
                result.append(current_char + str(count))
                current_char = data[i]
                count = 1
        result.append(current_char + str(count))
        return "".join(result)

    def decompress(self, data):
        if not data:
            return ""
        result = []
        i = 0
        while i < len(data):
            char = data[i]
            i += 1
            num_str = ""
            while i < len(data) and data[i].isdigit():
                num_str += data[i]
                i += 1
            count = int(num_str)
            result.append(char * count)
        return "".join(result)

if __name__ == '__main__':
    encoder = RunLengthEncoder()
    test_string_1 = "aaabbbccccdddd"
    test_string_2 = "a12b5"
    compressed_1 = encoder.compress(test_string_1)
    decompressed_1 = encoder.decompress(compressed_1)
    decompressed_2 = encoder.decompress(test_string_2)
    print(compressed_1)
    print(decompressed_1)
    print(decompressed_2)