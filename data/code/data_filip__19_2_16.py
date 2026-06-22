class RLECompressor:
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
                result.append(f"{count}{current_char}")
                current_char = char
                count = 1
        result.append(f"{count}{current_char}")
        return "".join(result)

    @staticmethod
    def decompress(data):
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
                count = int(count_str)
                char = data[i]
                result.append(char * count)
                i += 1
        return "".join(result)

    @staticmethod
    def compress_iterator(data):
        if not data:
            return iter([])
        current_char = data[0]
        count = 1
        for char in data[1:]:
            if char == current_char:
                count += 1
            else:
                yield f"{count}{current_char}"
                current_char = char
                count = 1
        yield f"{count}{current_char}"

    @staticmethod
    def decompress_iterator(data):
        if not data:
            return iter([])
        i = 0
        length = len(data)
        while i < length:
            count_str = ""
            while i < length and data[i].isdigit():
                count_str += data[i]
                i += 1
            if i < length:
                count = int(count_str)
                char = data[i]
                yield char * count
                i += 1

if __name__ == "__main__":
    sample_input = "AAABBBCCCCDDDEEEFF"
    compressor = RLECompressor()
    compressed = compressor.compress(sample_input)
    print(compressed)
    decompressed = compressor.decompress(compressed)
    print(decompressed)
    iterator_compressed = list(compressor.compress_iterator("XXXXYYYYZ"))
    print("".join(iterator_compressed))
    iterator_decompressed = "".join(compressor.decompress_iterator("3X4Y1Z"))
    print(iterator_decompressed)