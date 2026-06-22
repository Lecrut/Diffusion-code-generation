class RLE:
    @staticmethod
    def compress(data: str) -> str:
        if not data:
            return ""
        result = []
        current_char = data[0]
        count = 1
        for char in data[1:]:
            if char == current_char:
                count += 1
            else:
                result.append(f"{count}{current_char}")
                current_char = char
                count = 1
        result.append(f"{count}{current_char}")
        return "".join(result)

    @staticmethod
    def decompress(data: str) -> str:
        if not data:
            return ""
        result = []
        i = 0
        length = len(data)
        while i < length:
            count_str = ""
            while i < length and data[i].isdigit():
                count_str += data[i]
                i += 1
            if i < length:
                char = data[i]
                count = int(count_str)
                result.append(char * count)
                i += 1
        return "".join(result)

if __name__ == '__main__':
    rle = RLE()
    compressed = rle.compress("AAABBBCCCC")
    print(compressed)
    decompressed = rle.decompress(compressed)
    print(decompressed)