class RunLengthCompression:
    @staticmethod
    def compress(data: bytes) -> list:
        if not data:
            return []
        result = []
        current_byte = data[0]
        count = 1
        for i in range(1, len(data)):
            if data[i] == current_byte:
                count += 1
            else:
                result.append((current_byte, count))
                current_byte = data[i]
                count = 1
        result.append((current_byte, count))
        return result

    @staticmethod
    def decompress(compressed: list) -> bytes:
        if not compressed:
            return b""
        result = bytearray()
        for byte, count in compressed:
            result.extend(bytes([byte]) * count)
        return bytes(result)

if __name__ == '__main__':
    test_data = b"AABBBCCCC"
    compressor = RunLengthCompression()
    compressed = compressor.compress(test_data)
    decompressed = compressor.decompress(compressed)
    print(compressed)
    print(decompressed)
    print(test_data == decompressed)