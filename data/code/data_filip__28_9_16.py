class ByteRLE:
    @staticmethod
    def compress(data: bytes) -> list[tuple[int, int]]:
        if not data:
            return []
        
        result = []
        current_byte = data[0]
        count = 1
        
        for i in range(1, len(data)):
            if data[i] == current_byte and count < 255:
                count += 1
            else:
                result.append((current_byte, count))
                current_byte = data[i]
                count = 1
        
        result.append((current_byte, count))
        return result

    @staticmethod
    def decompress(compressed: list[tuple[int, int]]) -> bytes:
        if not compressed:
            return b""
        
        result = bytearray()
        for byte_val, count in compressed:
            result.extend([byte_val] * count)
        return bytes(result)

if __name__ == '__main__':
    sample_data = bytes([65, 65, 65, 66, 66, 67, 67, 67, 67, 67])
    compressed = ByteRLE.compress(sample_data)
    print(compressed)
    decompressed = ByteRLE.decompress(compressed)
    print(decompressed)