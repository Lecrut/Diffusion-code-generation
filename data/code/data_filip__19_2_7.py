from itertools import groupby

class RLECompressor:
    def compress(self, data: str) -> str:
        if not data:
            return ""
        result = []
        for char, group in groupby(data):
            count = sum(1 for _ in group)
            result.append(f"{char}{count}")
        return "".join(result)

    def decompress(self, compressed: str) -> str:
        result = []
        i = 0
        n = len(compressed)
        while i < n:
            char = compressed[i]
            i += 1
            num_str = ""
            while i < n and compressed[i].isdigit():
                num_str += compressed[i]
                i += 1
            if not num_str:
                num_str = "1"
            count = int(num_str)
            result.append(char * count)
        return "".join(result)

    def compress_iterator(self, data: str):
        if not data:
            return
        for char, group in groupby(data):
            count = sum(1 for _ in group)
            yield f"{char}{count}"

    def decompress_iterator(self, compressed: str):
        n = len(compressed)
        i = 0
        while i < n:
            char = compressed[i]
            i += 1
            num_str = ""
            while i < n and compressed[i].isdigit():
                num_str += compressed[i]
                i += 1
            if not num_str:
                num_str = "1"
            count = int(num_str)
            yield char * count

    def decompress_stream(self, compressed: str) -> str:
        return "".join(self.decompress_iterator(compressed))

if __name__ == '__main__':
    sample_input = "aaabbbcccaaa"
    compressor = RLECompressor()
    compressed = compressor.compress(sample_input)
    decompressed = compressor.decompress(compressed)
    print(f"Original: {sample_input}")
    print(f"Compressed: {compressed}")
    print(f"Decompressed: {decompressed}")
    iterator_result = list(compressor.compress_iterator("xxxyyyzz"))
    print(f"Iterator Compress: {iterator_result}")
    stream_result = compressor.decompress_stream("x3y3z2")
    print(f"Stream Decompress: {stream_result}")