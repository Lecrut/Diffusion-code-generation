import sys

class ByteRunLengthEncoder:
    MAX_RUN_LENGTH = 255
    
    @staticmethod
    def compress(data: bytes) -> bytes:
        if len(data) == 0:
            return b""
        encoded = bytearray()
        idx = 0
        total_len = len(data)
        while idx < total_len:
            current_val = data[idx]
            run_count = 1
            while (idx + run_count < total_len and 
                   run_count < ByteRunLengthEncoder.MAX_RUN_LENGTH and 
                   data[idx + run_count] == current_val):
                run_count += 1
            encoded.append(run_count)
            encoded.append(current_val)
            idx += run_count
        return bytes(encoded)
    
    @staticmethod
    def decompress(data: bytes) -> bytes:
        if len(data) % 2 != 0:
            raise ValueError("Invalid compressed data: length must be even")
        decoded = bytearray()
        for i in range(0, len(data), 2):
            count = data[i]
            byte_val = data[i + 1]
            decoded.extend([byte_val] * count)
        return bytes(decoded)

if __name__ == '__main__':
    sample_input = bytes([1, 1, 1, 2, 2, 3, 3, 3, 3, 3, 4, 5, 5, 5, 5])
    compressed = ByteRunLengthEncoder.compress(sample_input)
    decompressed = ByteRunLengthEncoder.decompress(compressed)
    print(compressed)
    print(decompressed)
    print("Match:", sample_input == decompressed)