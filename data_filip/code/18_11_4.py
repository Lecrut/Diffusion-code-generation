class RunLengthEncoder:
    @staticmethod
    def compress(data):
        if not data:
            return ""
        result = []
        current_char = data[0]
        count = 1
        for i in range(1, len(data)):
            if data[i] == current_char:
                count += 1
            else:
                result.append(str(count) + current_char)
                current_char = data[i]
                count = 1
        result.append(str(count) + current_char)
        return "".join(result)

    @staticmethod
    def decompress(data):
        if not data:
            return ""
        result = []
        i = 0
        while i < len(data):
            num_str = ""
            while i < len(data) and data[i].isdigit():
                num_str += data[i]
                i += 1
            count = int(num_str)
            if i < len(data):
                char = data[i]
                result.append(char * count)
                i += 1
        return "".join(result)

if __name__ == "__main__":
    sample_compressed = RunLengthEncoder.compress("AAABBBCCCCDDDD")
    print(sample_compressed)
    sample_decompressed = RunLengthEncoder.decompress(sample_compressed)
    print(sample_decompressed)
    mixed_data = "WWWWWWWWWWWWBWWWWWWWWWWWWWWBWWWWWWWWWWWWWWB"
    compressed_mixed = RunLengthEncoder.compress(mixed_data)
    print(compressed_mixed)
    decompressed_mixed = RunLengthEncoder.decompress(compressed_mixed)
    print(decompressed_mixed)