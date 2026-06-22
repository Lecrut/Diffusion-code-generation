class RunLengthEncoder:
    @staticmethod
    def compress(data):
        if not data:
            return []
        result = []
        current_char = data[0]
        count = 1
        for i in range(1, len(data)):
            if data[i] == current_char:
                count += 1
            else:
                result.append((current_char, count))
                current_char = data[i]
                count = 1
        result.append((current_char, count))
        return result

    @staticmethod
    def decompress(encoded_data):
        if not encoded_data:
            return ""
        result = []
        for char, count in encoded_data:
            result.append(char * count)
        return "".join(result)

if __name__ == '__main__':
    sample_input = "aaabbccccdd"
    compressed = RunLengthEncoder.compress(sample_input)
    decompressed = RunLengthEncoder.decompress(compressed)
    print(compressed)
    print(decompressed)