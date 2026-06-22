class RunLengthCompressor:
    @staticmethod
    def compress(data: bytes) -> bytes:
        if not data:
            return b''
        result = bytearray()
        i = 0
        n = len(data)
        while i < n:
            current_byte = data[i]
            count = 1
            while i + count < n and data[i + count] == current_byte and count < 255:
                count += 1
            result.append(count)
            result.append(current_byte)
            i += count
        return bytes(result)

    @staticmethod
    def decompress(data: bytes) -> bytes:
        if not data:
            return b''
        result = bytearray()
        i = 0
        n = len(data)
        while i < n:
            if i + 1 >= n:
                raise ValueError("Malformed compressed data")
            count = data[i]
            byte_val = data[i + 1]
            result.extend(bytes([byte_val]) * count)
            i += 2
        return bytes(result)

if __name__ == '__main__':
    original = b'AAAAABBBCCDDEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE'
    compressed = RunLengthCompressor.compress(original)
    decompressed = RunLengthCompressor.decompress(compressed)
    print(original)
    print(compressed)
    print(decompressed)
    print(original == decompressed)