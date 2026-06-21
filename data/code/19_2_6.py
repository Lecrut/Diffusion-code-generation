import itertools
from collections.abc import Iterator

class RLECompressor:
    @staticmethod
    def compress(data: str) -> str:
        if not data:
            return ""
        
        result = []
        for char, group in itertools.groupby(data):
            count = sum(1 for _ in group)
            result.append(f"{count}{char}")
        
        return "".join(result)

    @staticmethod
    def decompress(data: str) -> str:
        if not data:
            return ""
        
        result = []
        count_str = []
        
        for char in data:
            if char.isdigit():
                count_str.append(char)
            else:
                if count_str:
                    count = int("".join(count_str))
                    result.append(char * count)
                    count_str = []
                else:
                    result.append(char)
        
        if count_str:
            raise ValueError("Invalid RLE data: ends with a count digit without a character")
        
        return "".join(result)

    @staticmethod
    def compress_iterator(data: str) -> Iterator[tuple[int, str]]:
        if not data:
            return
        for char, group in itertools.groupby(data):
            yield sum(1 for _ in group), char

    @staticmethod
    def decompress_iterator(data: str) -> Iterator[str]:
        if not data:
            return
        
        count_str = []
        for char in data:
            if char.isdigit():
                count_str.append(char)
            else:
                if count_str:
                    count = int("".join(count_str))
                    for _ in range(count):
                        yield char
                    count_str = []
                else:
                    yield char
        
        if count_str:
            raise ValueError("Invalid RLE data: ends with a count digit without a character")

if __name__ == '__main__':
    sample_input = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW"
    compressed = RLECompressor.compress(sample_input)
    decompressed = RLECompressor.decompress(compressed)
    iter_compressed = list(RLECompressor.compress_iterator(sample_input))
    iter_decompressed = "".join(RLECompressor.decompress_iterator(compressed))
    
    print(f"Original: {sample_input}")
    print(f"Compressed: {compressed}")
    print(f"Decompressed: {decompressed}")
    print(f"Iterator Compressed Tuples: {iter_compressed}")
    print(f"Iterator Decompressed Reconstructed: {iter_decompressed}")
    print(f"Match Check: {sample_input == decompressed == iter_decompressed}")