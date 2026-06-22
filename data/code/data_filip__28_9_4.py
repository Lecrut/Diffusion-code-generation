class RunLengthCompressor:
    @staticmethod
    def compress(data: bytes) -> bytes:
        if not data:
            return b""
        
        compressed = bytearray()
        count = 1
        current_byte = data[0]
        
        for i in range(1, len(data)):
            if data[i] == current_byte:
                count += 1
                if count == 255:
                    compressed.append(current_byte)
                    compressed.append(255)
                    count = 0
            else:
                if count > 0:
                    if count == 1:
                        compressed.append(current_byte)
                    else:
                        compressed.append(current_byte)
                        compressed.append(count)
                current_byte = data[i]
                count = 1
        
        if count > 0:
            if count == 1:
                compressed.append(current_byte)
            else:
                compressed.append(current_byte)
                compressed.append(count)
        
        return bytes(compressed)
    
    @staticmethod
    def decompress(data: bytes) -> bytes:
        if not data:
            return b""
        
        decompressed = bytearray()
        i = 0
        while i < len(data):
            byte = data[i]
            i += 1
            if i < len(data) and data[i] == 255:
                decompressed.extend([byte] * 255)
                i += 1
            elif i < len(data):
                count = data[i]
                if count == 0:
                    decompressed.extend([byte] * 255)
                else:
                    decompressed.extend([byte] * count)
                i += 1
            else:
                decompressed.append(byte)
        
        return bytes(decompressed)

if __name__ == '__main__':
    sample_data = b"AAABBBCCCCCCDDDDDDDD"
    compressed = RunLengthCompressor.compress(sample_data)
    decompressed = RunLengthCompressor.decompress(compressed)
    print(compressed)
    print(decompressed)
    print(sample_data == decompressed)