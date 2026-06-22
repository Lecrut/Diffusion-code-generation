class RunLengthEncoder:
    @staticmethod
    def compress(data: bytes) -> list:
        if not data:
            return []
        
        compressed = []
        current_byte = data[0]
        count = 1
        
        for i in range(1, len(data)):
            byte = data[i]
            if byte == current_byte and count < 255:
                count += 1
            else:
                compressed.append((current_byte, count))
                current_byte = byte
                count = 1
        
        compressed.append((current_byte, count))
        return compressed

    @staticmethod
    def decompress(compressed_data: list) -> bytes:
        if not compressed_data:
            return b''
        
        decompressed = bytearray()
        
        for byte, count in compressed_data:
            decompressed.extend([byte] * count)
        
        return bytes(decompressed)

if __name__ == '__main__':
    sample_data = b"AAABBBCCCA"
    
    compressed = RunLengthEncoder.compress(sample_data)
    
    decompressed = RunLengthEncoder.decompress(compressed)
    
    print(compressed)
    print(decompressed)
    print(decompressed == sample_data)