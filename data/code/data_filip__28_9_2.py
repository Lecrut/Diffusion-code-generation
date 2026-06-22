class RLCByteCompressor:
    @staticmethod
    def compress(data: bytes) -> bytes:
        if not data:
            return b''
        
        result = bytearray()
        n = len(data)
        i = 0
        
        while i < n:
            current_byte = data[i]
            run_length = 1
            
            while i + run_length < n and data[i + run_length] == current_byte:
                run_length += 1
            
            if run_length >= 4:
                if current_byte == 0xFF:
                    result.append(0xFF)
                    result.append(0x00)
                else:
                    result.append(0xFF)
                    result.append(current_byte)
                    result.append(run_length - 3)
                i += run_length
            else:
                for _ in range(run_length):
                    if current_byte == 0xFF:
                        result.append(0xFF)
                        result.append(0x00)
                    else:
                        result.append(current_byte)
                i += run_length
        
        return bytes(result)

    @staticmethod
    def decompress(data: bytes) -> bytes:
        if not data:
            return b''
        
        result = bytearray()
        n = len(data)
        i = 0
        
        while i < n:
            byte = data[i]
            
            if byte == 0xFF and i + 1 < n:
                next_byte = data[i + 1]
                if next_byte == 0x00:
                    result.append(0xFF)
                    i += 2
                else:
                    run_length = next_byte + 3
                    for _ in range(run_length):
                        result.append(byte)
                    i += 2
            else:
                result.append(byte)
                i += 1
        
        return bytes(result)

if __name__ == '__main__':
    original = b'AAAABBBBCCCCDDDD'
    compressed = RLCByteCompressor.compress(original)
    decompressed = RLCByteCompressor.decompress(compressed)
    print(f'Original: {original}')
    print(f'Compressed: {compressed}')
    print(f'Decompressed: {decompressed}')
    print(f'Match: {original == decompressed}')