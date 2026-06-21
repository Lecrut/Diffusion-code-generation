class ByteRunLengthEncoder:
    HEADER_RUN_FLAG = 0x00
    MAX_RUN_LENGTH = 0xFF

    @staticmethod
    def compress(data: bytes) -> bytes:
        if not data:
            return b''
        output = bytearray()
        idx = 0
        total_len = len(data)
        while idx < total_len:
            current_val = data[idx]
            count = 1
            while idx + count < total_len and count < ByteRunLengthEncoder.MAX_RUN_LENGTH and data[idx + count] == current_val:
                count += 1
            output.append(current_val)
            output.append(count)
            idx += count
        return bytes(output)

    @staticmethod
    def decompress(compressed_data: bytes) -> bytes:
        if not compressed_data:
            return b''
        if len(compressed_data) % 2 != 0:
            raise ValueError("Invalid compressed data length")
        output = bytearray()
        idx = 0
        while idx < len(compressed_data):
            value = compressed_data[idx]
            count = compressed_data[idx + 1]
            output.extend([value] * count)
            idx += 2
        return bytes(output)

if __name__ == '__main__':
    sample_input = b'A' * 10 + b'B' * 5 + b'C' * 3 + b'D' * 1
    encoded = ByteRunLengthEncoder.compress(sample_input)
    decoded = ByteRunLengthEncoder.decompress(encoded)
    print(f"Original: {list(sample_input)}")
    print(f"Compressed: {list(encoded)}")
    print(f"Decompressed: {list(decoded)}")
    print(f"Match: {sample_input == decoded}")