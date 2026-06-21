class RunLengthEncoder:
    @staticmethod
    def compress(data: bytes) -> bytes:
        if not data:
            return b''
        result = bytearray()
        current_byte = data[0]
        count = 1
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
            return b''
        result = bytearray()
        if len(data) % 2 != 0:
            raise ValueError("Invalid compressed data: odd length")
        for i in range(0, len(data), 2):
            count = data[i]
            byte_val = data[i + 1]
            result.extend([byte_val] * count)
        return bytes(result)

if __name__ == '__main__':
    original = b'A' * 10 + b'B' * 5 + b'C' * 2 + b'A' * 3
    compressed = RunLengthEncoder.compress(original)
    decompressed = RunLengthEncoder.decompress(compressed)
    print(original)
    print(compressed)
    print(decompressed)