class RunLengthCompressor:
    @staticmethod
    def compress(data: bytes) -> bytes:
        if not data:
            return b''
        
        compressed = bytearray()
        i = 0
        n = len(data)
        
        while i < n:
            current_byte = data[i]
            count = 1
            while i + count < n and data[i + count] == current_byte and count < 255:
                count += 1
            
            if count == 1:
                compressed.append(0)
                compressed.append(current_byte)
            else:
                compressed.append(count)
                compressed.append(current_byte)
            
            i += count
        
        return bytes(compressed)
    
    @staticmethod
    def decompress(data: bytes) -> bytes:
        if not data:
            return b''
        
        decompressed = bytearray()
        i = 0
        n = len(data)
        
        while i < n:
            if i + 1 >= n:
                raise ValueError("Invalid compressed data: incomplete pair")
            
            count_byte = data[i]
            value_byte = data[i + 1]
            
            if count_byte == 0:
                decompressed.append(value_byte)
            else:
                decompressed.extend(bytes([value_byte] * count_byte))
            
            i += 2
        
        return bytes(decompressed)

if __name__ == '__main__':
    sample_data = b'AAABBBCCDEEEEFFFFFGGGHHIIIIIIIIIIIJJKKKLLLMMMMNNNNOOOOPPPQQQQRRRSTTTUUUVVVWWXYYZZ'
    compressor = RunLengthCompressor()
    
    compressed = compressor.compress(sample_data)
    decompressed = compressor.decompress(compressed)
    
    print(sample_data)
    print(compressed)
    print(decompressed)
    print(sample_data == decompressed)
    
    sample_data2 = b''
    compressed2 = compressor.compress(sample_data2)
    decompressed2 = compressor.decompress(compressed2)
    print(compressed2)
    print(decompressed2)
    
    sample_data3 = b'\x00\x01\x02\x03\x04\x05'
    compressed3 = compressor.compress(sample_data3)
    decompressed3 = compressor.decompress(compressed3)
    print(compressed3)
    print(decompressed3)
    print(sample_data3 == decompressed3)