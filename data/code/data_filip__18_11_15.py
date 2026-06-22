class RunLengthEncoder:
    @staticmethod
    def compress(data):
        if not data:
            return []
        result = []
        current_char = data[0]
        count = 1
        for char in data[1:]:
            if char == current_char:
                count += 1
            else:
                result.append((current_char, count))
                current_char = char
                count = 1
        result.append((current_char, count))
        return result

    @staticmethod
    def decompress(encoded_data):
        result = []
        for char, count in encoded_data:
            result.extend([char] * count)
        return result

if __name__ == '__main__':
    test_string = "WWWWWWWWWWWWBWWWWWWWWWWWWBBB"
    compressed = RunLengthEncoder.compress(test_string)
    print(compressed)
    decompressed = RunLengthEncoder.decompress(compressed)
    print("".join(decompressed))
    print("".join(decompressed) == test_string)