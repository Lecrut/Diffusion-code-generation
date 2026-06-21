class RunLengthCompressor:
    @staticmethod
    def compress(data: bytes) -> bytes:
        if not data:
            return b""
        
        result = bytearray()
        count = 1
        current_byte = data[0]
        
        for i in range(1, len(data)):
            if data[i] == current_byte and count < 255:
                count += 1
            else:
                result.append(count)
                result.append(current_byte)
                current_byte = data[i]
                count = 1
        
        result.append(count)
        result.append(current_byte)
        return bytes(result)

    @staticmethod
    def decompress(data: bytes) -> bytes:
        if not data:
            return b""
        
        if len(data) % 2 != 0:
            raise ValueError("Compressed data must have even length")
        
        result = bytearray()
        for i in range(0, len(data), 2):
            count = data[i]
            byte_val = data[i + 1]
            result.extend([byte_val] * count)
        return bytes(result)

if __name__ == '__main__':
    original = b"AAABBBCCD"
    compressed = RunLengthCompressor.compress(original)
    decompressed = RunLengthCompressor.decompress(compressed)
    print(original)
    print(compressed)
    print(decompressed)
    print(original == decompressed)