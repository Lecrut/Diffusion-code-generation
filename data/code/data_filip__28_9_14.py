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
        if len(data) % 2 != 0:
            raise ValueError("Invalid compressed data length")
        result = bytearray()
        for i in range(0, len(data), 2):
            count = data[i]
            byte = data[i + 1]
            result.extend([byte] * count)
        return bytes(result)

if __name__ == '__main__':
    sample_data = b'AAAABBBCCDAA'
    compressed = RunLengthEncoder.compress(sample_data)
    decompressed = RunLengthEncoder.decompress(compressed)
    print(compressed)
    print(decompressed)