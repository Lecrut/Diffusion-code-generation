class RunLengthEncoder:
    @staticmethod
    def compress(data: str) -> str:
        if not data:
            return ""
        compressed = []
        current_char = data[0]
        count = 1
        for char in data[1:]:
            if char == current_char:
                count += 1
            else:
                compressed.append(f"{count}{current_char}")
                current_char = char
                count = 1
        compressed.append(f"{count}{current_char}")
        return "".join(compressed)

    @staticmethod
    def decompress(encoded_data: str) -> str:
        if not encoded_data:
            return ""
        decoded = []
        i = 0
        while i < len(encoded_data):
            count_str = ""
            while i < len(encoded_data) and encoded_data[i].isdigit():
                count_str += encoded_data[i]
                i += 1
            if i < len(encoded_data):
                count = int(count_str)
                char = encoded_data[i]
                decoded.append(char * count)
                i += 1
        return "".join(decoded)

if __name__ == '__main__':
    sample_compressed = RunLengthEncoder.compress("aaabbbccccdd")
    print(sample_compressed)
    sample_decompressed = RunLengthEncoder.decompress(sample_compressed)
    print(sample_decompressed)
    another_compressed = RunLengthEncoder.compress("AABBCCC")
    print(another_compressed)
    another_decompressed = RunLengthEncoder.decompress("3A2B3C")
    print(another_decompressed)