import sys
from typing import Iterable, Iterator, Tuple, List, Optional

class RLECompressor:
    def __init__(self, max_chunk_size: int = 1000000):
        self.max_chunk_size = max_chunk_size

    def compress(self, data: str) -> str:
        if not data:
            return ""
        
        result = []
        current_char = data[0]
        count = 1
        
        for char in data[1:]:
            if char == current_char:
                count += 1
                if count >= self.max_chunk_size:
                    result.append(f"{count}{current_char}")
                    current_char = data[data.index(char) + 1] if data.index(char) + 1 < len(data) else ''
                    count = 1
                    if not current_char:
                        break
            else:
                result.append(f"{count}{current_char}")
                current_char = char
                count = 1
        
        if count > 0:
            result.append(f"{count}{current_char}")
        
        return "".join(result)

    def decompress(self, compressed: str) -> str:
        if not compressed:
            return ""
        
        result = []
        i = 0
        n = len(compressed)
        
        while i < n:
            count_str = ""
            while i < n and compressed[i].isdigit():
                count_str += compressed[i]
                i += 1
            
            if not count_str or i >= n:
                break
            
            count = int(count_str)
            char = compressed[i]
            i += 1
            
            result.append(char * count)
        
        return "".join(result)

    def compress_stream(self, data: str) -> Iterator[str]:
        if not data:
            return
        
        current_char = data[0]
        count = 1
        
        for char in data[1:]:
            if char == current_char:
                count += 1
                if count >= self.max_chunk_size:
                    yield f"{count}{current_char}"
                    current_char = char
                    count = 1
            else:
                yield f"{count}{current_char}"
                current_char = char
                count = 1
        
        if count > 0:
            yield f"{count}{current_char}"

    def decompress_stream(self, compressed: str) -> Iterator[str]:
        if not compressed:
            return
        
        i = 0
        n = len(compressed)
        
        while i < n:
            count_str = ""
            while i < n and compressed[i].isdigit():
                count_str += compressed[i]
                i += 1
            
            if not count_str or i >= n:
                break
            
            count = int(count_str)
            char = compressed[i]
            i += 1
            
            yield char * count

if __name__ == '__main__':
    sample_text = "AAABBBCCCCDDDDDDDDEEEEEEE"
    compressor = RLECompressor()
    
    compressed = compressor.compress(sample_text)
    decompressed = compressor.decompress(compressed)
    
    print(f"Original: {sample_text}")
    print(f"Compressed: {compressed}")
    print(f"Decompressed: {decompressed}")
    
    compressed_stream = "".join(list(compressor.compress_stream(sample_text)))
    decompressed_stream = "".join(list(compressor.decompress_stream(compressed_stream)))
    
    print(f"Stream Compressed: {compressed_stream}")
    print(f"Stream Decompressed: {decompressed_stream}")