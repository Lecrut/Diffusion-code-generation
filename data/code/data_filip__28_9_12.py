import struct
from typing import List, Tuple, Union

class RunLengthCompressor:
    MAX_RUN_LENGTH = 255

    @staticmethod
    def compress(data: bytes) -> bytes:
        if not data:
            return b""
        
        result = bytearray()
        current_byte = data[0]
        count = 1
        
        for i in range(1, len(data)):
            byte = data[i]
            if byte == current_byte and count < RunLengthCompressor.MAX_RUN_LENGTH:
                count += 1
            else:
                result.append(count)
                result.append(current_byte)
                current_byte = byte
                count = 1
        
        result.append(count)
        result.append(current_byte)
        
        return bytes(result)

    @staticmethod
    def decompress(compressed_data: bytes) -> bytes:
        if len(compressed_data) % 2 != 0:
            raise ValueError("Invalid compressed data length")
        
        result = bytearray()
        iterator = iter(compressed_data)
        
        for count in iterator:
            byte = next(iterator)
            result.extend([byte] * count)
        
        return bytes(result)

if __name__ == '__main__':
    sample_data = b'A' * 10 + b'B' * 3 + b'C' * 255 + b'D' * 2
    compressed = RunLengthCompressor.compress(sample_data)
    decompressed = RunLengthCompressor.decompress(compressed)
    print(compressed)
    print(decompressed)