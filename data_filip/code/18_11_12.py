class RunLengthEncoder:
    @staticmethod
    def compress(input_str: str) -> str:
        if not input_str:
            return ""
        result = []
        count = 1
        current_char = input_str[0]
        for i in range(1, len(input_str)):
            if input_str[i] == current_char:
                count += 1
            else:
                result.append(f"{count}{current_char}")
                current_char = input_str[i]
                count = 1
        result.append(f"{count}{current_char}")
        return "".join(result)

    @staticmethod
    def decompress(input_str: str) -> str:
        if not input_str:
            return ""
        result = []
        num_str = []
        for char in input_str:
            if char.isdigit():
                num_str.append(char)
            else:
                count = int("".join(num_str))
                result.append(char * count)
                num_str = []
        return "".join(result)

if __name__ == '__main__':
    encoder = RunLengthEncoder()
    original_text = "AAABBBCC"
    compressed = RunLengthEncoder.compress(original_text)
    decompressed = RunLengthEncoder.decompress(compressed)
    print(f"Original: {original_text}")
    print(f"Compressed: {compressed}")
    print(f"Decompressed: {decompressed}")