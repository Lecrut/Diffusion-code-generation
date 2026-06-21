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
    def decompress(compressed):
        return [char * count for char, count in compressed]

if __name__ == '__main__':
    encoder = RunLengthEncoder()
    sample_string = "AAABBBCCCDAA"
    compressed = encoder.compress(sample_string)
    print(compressed)
    decompressed = encoder.decompress(compressed)
    print(decompressed)