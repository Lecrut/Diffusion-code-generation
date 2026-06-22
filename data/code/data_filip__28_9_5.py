class RunLengthCompressor:
    @staticmethod
    def compress(data: bytes) -> bytes:
        if not data:
            return b''
        
        result = bytearray()
        count = 1
        current_byte = data[0]
        
        for i in range(1, len(data)):
            if data[i] == current_byte and count < 255:
                count += 1
            else:
                if count == 1:
                    result.append(current_byte)
                    result.append(1)
                else:
                    result.append(count)
                    result.append(current_byte)
                count = 1
                current_byte = data[i]
        
        if count == 1:
            result.append(current_byte)
            result.append(1)
        else:
            result.append(count)
            result.append(current_byte)
            
        return bytes(result)

    @staticmethod
    def decompress(data: bytes) -> bytes:
        if not data:
            return b''
        
        result = bytearray()
        i = 0
        length = len(data)
        
        while i < length:
            count = data[i]
            i += 1
            value = data[i]
            i += 1
            result.extend([value] * count)
            
        return bytes(result)

if __name__ == '__main__':
    compressor = RunLengthCompressor()
    sample_data = b'AABBCCCDDDDD'
    compressed = compressor.compress(sample_data)
    decompressed = compressor.decompress(compressed)
    print(compressed)
    print(decompressed)