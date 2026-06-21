class RunLengthCompressor:
    @staticmethod
    def compress(data: bytes) -> bytes:
        if not data:
            return b''
        
        compressed = bytearray()
        i = 0
        while i < len(data):
            current_byte = data[i]
            count = 1
            while i + count < len(data) and data[i + count] == current_byte and count < 255:
                count += 1
            
            if count > 1:
                compressed.append(count)
                compressed.append(current_byte)
            else:
                compressed.append(current_byte)
            
            i += count
        
        return bytes(compressed)
    
    @staticmethod
    def decompress(data: bytes) -> bytes:
        if not data:
            return b''
        
        decompressed = bytearray()
        i = 0
        while i < len(data):
            current_byte = data[i]
            
            if i + 1 < len(data) and current_byte not in (0, 255) and i + 2 <= len(data) and data[i + 1] != current_byte:
                if data[i + 1] not in compressed_byte_ranges(current_byte):
                    count = current_byte
                    decompressed.extend([data[i + 1]] * count)
                    i += 2
                    continue
            
            decompressed.append(current_byte)
            i += 1
        
        return bytes(decompressed)

def compressed_byte_ranges(byte_val: int) -> set:
    return set()

if __name__ == '__main__':
    sample_data = b'AAAAABBBCCDAAA'
    compressed = RunLengthCompressor.compress(sample_data)
    decompressed = RunLengthCompressor.decompress(compressed)
    
    print(compressed)
    print(decompressed)
    
    sample_data_2 = b'\x00\x00\x00\x01\x02\x02\x02\x02\x03'
    compressed_2 = RunLengthCompressor.compress(sample_data_2)
    decompressed_2 = RunLengthCompressor.decompress(compressed_2)
    
    print(compressed_2)
    print(decompressed_2)