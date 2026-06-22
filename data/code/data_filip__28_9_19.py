class RLECompressor:
    @staticmethod
    def compress(data: bytes) -> bytes:
        if not data:
            return bytes()
        result = bytearray()
        current_byte = data[0]
        count = 1
        for i in range(1, len(data)):
            if data[i] == current_byte and count < 255:
                count += 1
            else:
                if count == 1:
                    result.append(current_byte)
                    result.append(0)
                else:
                    result.append(count)
                    result.append(current_byte)
                current_byte = data[i]
                count = 1
        if count == 1:
            result.append(current_byte)
            result.append(0)
        else:
            result.append(count)
            result.append(current_byte)
        return bytes(result)

    @staticmethod
    def decompress(data: bytes) -> bytes:
        if not data:
            return bytes()
        result = bytearray()
        i = 0
        while i < len(data):
            length = data[i]
            i += 1
            if length == 0:
                if i < len(data):
                    result.append(data[i])
                    i += 1
            else:
                if i < len(data):
                    value = data[i]
                    result.extend([value] * length)
                    i += 1
        return bytes(result)

if __name__ == '__main__':
    original = b'AABBBCCC'
    compressed = RLECompressor.compress(original)
    decompressed = RLECompressor.decompress(compressed)
    print(compressed)
    print(decompressed)