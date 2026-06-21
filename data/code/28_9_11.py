class RunLengthCompressor:
    @staticmethod
    def compress(data: bytes) -> bytes:
        if not data:
            return b''
        
        result = bytearray()
        i = 0
        n = len(data)
        
        while i < n:
            current_byte = data[i]
            count = 1
            
            while i + count < n and data[i + count] == current_byte:
                count += 1
                if count >= 127:
                    break
            
            if count == 1:
                result.append(0)
                result.append(current_byte)
            else:
                result.append(count)
                result.append(current_byte)
            
            i += count
        
        return bytes(result)
    
    @staticmethod
    def decompress(data: bytes) -> bytes:
        if not data:
            return b''
        
        result = bytearray()
        i = 0
        n = len(data)
        
        while i < n:
            if i + 1 >= n:
                break
            
            count = data[i]
            byte = data[i + 1]
            
            if count == 0:
                result.append(byte)
            else:
                result.extend([byte] * count)
            
            i += 2
        
        return bytes(result)

if __name__ == '__main__':
    sample_data = b'AAABBBCCDAAAAAEEEEEEF'
    compressed = RunLengthCompressor.compress(sample_data)
    decompressed = RunLengthCompressor.decompress(compressed)
    
    print(compressed)
    print(decompressed)
    print(sample_data == decompressed)