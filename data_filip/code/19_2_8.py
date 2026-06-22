class RLECompressor:
    def __init__(self):
        self.compressed_cache = ""
        self.decompressed_cache = ""

    def compress(self, data):
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
        self.compressed_cache = "".join(result)
        return self.compressed_cache

    def decompress(self, data):
        if not data:
            return ""
        result = []
        i = 0
        while i < len(data):
            count = 0
            while i < len(data) and data[i].isdigit():
                count = count * 10 + int(data[i])
                i += 1
            if i < len(data):
                char = data[i]
                result.append(char * count)
                i += 1
        self.decompressed_cache = "".join(result)
        return self.decompressed_cache

    def compress_generator(self, data):
        if not data:
            return
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

    def decompress_generator(self, data):
        if not data:
            return
        i = 0
        while i < len(data):
            count = 0
            while i < len(data) and data[i].isdigit():
                count = count * 10 + int(data[i])
                i += 1
            if i < len(data):
                char = data[i]
                for _ in range(count):
                    yield char
                i += 1

if __name__ == '__main__':
    compressor = RLECompressor()
    sample_string = "WWWWWWWWWWWWBWWWWWWWWWWWWBBB"
    compressed = compressor.compress(sample_string)
    decompressed = compressor.decompress(compressed)
    print(compressed)
    print(decompressed)
    gen_compressed = "".join(compressor.compress_generator(sample_string))
    gen_decompressed = "".join(compressor.decompress_generator(compressed))
    print(gen_compressed)
    print(gen_decompressed)