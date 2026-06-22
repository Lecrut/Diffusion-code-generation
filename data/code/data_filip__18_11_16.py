class RunLengthEncoder:
    @staticmethod
    def compress(data):
        if not data:
            return ""
        result = []
        current_char = data[0]
        count = 1
        for char in data[1:]:
            if char == current_char:
                count += 1
            else:
                result.append(f"{current_char}{count}")
                current_char = char
                count = 1
        result.append(f"{current_char}{count}")
        return "".join(result)

    @staticmethod
    def decompress(data):
        if not data:
            return ""
        result = []
        i = 0
        while i < len(data):
            char = data[i]
            i += 1
            count_str = []
            while i < len(data) and data[i].isdigit():
                count_str.append(data[i])
                i += 1
            count = int("".join(count_str)) if count_str else 1
            result.append(char * count)
        return "".join(result)

if __name__ == "__main__":
    sample_input = "AAAABBBCCDAAA"
    compressed = RunLengthEncoder.compress(sample_input)
    decompressed = RunLengthEncoder.decompress(compressed)
    print(compressed)
    print(decompressed)
    another_input = "WWWWWWWWWWWWBWWWWWWWWWWWWBBB"
    another_compressed = RunLengthEncoder.compress(another_input)
    another_decompressed = RunLengthEncoder.decompress(another_compressed)
    print(another_compressed)
    print(another_decompressed)