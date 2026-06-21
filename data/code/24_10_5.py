class RunLengthEncoder:
    def compress(self, data: str) -> str:
        if not data:
            return ""
        result = []
        count = 1
        current_char = data[0]
        for i in range(1, len(data)):
            if data[i] == current_char:
                count += 1
            else:
                result.append(f"{count}{current_char}")
                current_char = data[i]
                count = 1
        result.append(f"{count}{current_char}")
        return "".join(result)

    def decompress(self, data: str) -> str:
        if not data:
            return ""
        result = []
        count_str = ""
        for char in data:
            if char.isdigit():
                count_str += char
            else:
                count = int(count_str)
                result.append(char * count)
                count_str = ""
        return "".join(result)

if __name__ == '__main__':
    encoder = RunLengthEncoder()
    sample_input = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB"
    compressed = encoder.compress(sample_input)
    print(compressed)
    decompressed = encoder.decompress(compressed)
    print(decompressed)
    print(sample_input == decompressed)
    empty_test = ""
    print(encoder.compress(empty_test))
    print(encoder.decompress(empty_test))
    single_char = "A"
    print(encoder.compress(single_char))
    print(encoder.decompress(encoder.compress(single_char)))
    mixed = "AABCCCC"
    print(encoder.compress(mixed))
    print(encoder.decompress(encoder.compress(mixed)))