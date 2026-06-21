class RunLengthCompressor:
    @staticmethod
    def compress(data: bytes) -> list:
        if not data:
            return []
        
        compressed = []
        current_byte = data[0]
        count = 1
        
        for i in range(1, len(data)):
            if data[i] == current_byte:
                count += 1
            else:
                if count > 1:
                    compressed.append(count)
                    compressed.append(current_byte)
                else:
                    compressed.append(current_byte)
                current_byte = data[i]
                count = 1
        
        if count > 1:
            compressed.append(count)
            compressed.append(current_byte)
        else:
            compressed.append(current_byte)
            
        return compressed

    @staticmethod
    def decompress(compressed: list) -> bytes:
        if not compressed:
            return b''
        
        decompressed = bytearray()
        i = 0
        while i < len(compressed):
            value = compressed[i]
            if isinstance(value, int) and i + 1 < len(compressed) and i % 2 == 0:
                count = value
                byte_val = compressed[i + 1]
                decompressed.extend([byte_val] * count)
                i += 2
            else:
                decompressed.append(value)
                i += 1
        
        return bytes(decompressed)

if __name__ == '__main__':
    compressor = RunLengthCompressor()
    original_data = b'AABBCCCDDDD'
    compressed_data = compressor.compress(original_data)
    decompressed_data = compressor.decompress(compressed_data)
    print(compressed_data)
    print(decompressed_data)
    print(original_data == decompressed_data)