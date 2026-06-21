class RLE:
    @staticmethod
    def compress(data: str) -> str:
        if not data:
            return ""
        result = []
        current_char = data[0]
        count = 1
        for i in range(1, len(data)):
            char = data[i]
            if char == current_char:
                count += 1
            else:
                result.append(f"{count}{current_char}")
                current_char = char
                count = 1
        result.append(f"{count}{current_char}")
        return "".join(result)

    @staticmethod
    def decompress(encoded_data: str) -> str:
        if not encoded_data:
            return ""
        result = []
        i = 0
        while i < len(encoded_data):
            count = []
            while i < len(encoded_data) and encoded_data[i].isdigit():
                count.append(encoded_data[i])
                i += 1
            digit_str = "".join(count)
            char_count = int(digit_str) if digit_str else 1
            if i < len(encoded_data):
                char = encoded_data[i]
                result.append(char * char_count)
                i += 1
        return "".join(result)

if __name__ == '__main__':
    sample = "wwwwaaadexxxxxxwww"
    encoded = RLE.compress(sample)
    decoded = RLE.decompress(encoded)
    print(f"Original: {sample}")
    print(f"Compressed: {encoded}")
    print(f"Decompressed: {decoded}")
    print(f"Match: {sample == decoded}")

    empty = ""
    print(f"Empty Compressed: '{RLE.compress(empty)}'")
    print(f"Empty Decompressed: '{RLE.decompress(RLE.compress(empty))}'")

    single = "z"
    print(f"Single Compressed: '{RLE.compress(single)}'")
    print(f"Single Decompressed: '{RLE.decompress(RLE.compress(single))}'")