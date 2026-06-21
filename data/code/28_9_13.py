class RunLengthCompressor:

    @staticmethod
    def compress(data: bytes) -> list:
        if not data:
            return []
        
        result = []
        current_byte = data[0]
        count = 1
        length = len(data)
        
        i = 1
        while i < length:
            byte = data[i]
            if byte == current_byte and count < 255:
                count += 1
            else:
                result.append((current_byte, count))
                current_byte = byte
                count = 1
            i += 1
        
        result.append((current_byte, count))
        return result

    @staticmethod
    def decompress(rle_data: list) -> bytes:
        if not rle_data:
            return b''
        
        result = bytearray()
        for byte_val, count in rle_data:
            result.extend(bytes([byte_val]) * count)
        return bytes(result)

    @staticmethod
    def encode(data: bytes) -> bytes:
        rle_tuples = RunLengthCompressor.compress(data)
        encoded = bytearray()
        for byte_val, count in rle_tuples:
            encoded.append(count)
            encoded.append(byte_val)
        return bytes(encoded)

    @staticmethod
    def decode(encoded_data: bytes) -> bytes:
        if not encoded_data:
            return b''
        
        if len(encoded_data) % 2 != 0:
            raise ValueError("Encoded data must have even length.")
        
        decoded = bytearray()
        for i in range(0, len(encoded_data), 2):
            count = encoded_data[i]
            byte_val = encoded_data[i + 1]
            decoded.extend(bytes([byte_val]) * count)
        return bytes(decoded)

if __name__ == '__main__':
    sample_data = b"AAABBBCCCAAA"
    rle_list = RunLengthCompressor.compress(sample_data)
    print(rle_list)
    
    decompressed_bytes = RunLengthCompressor.decompress(rle_list)
    print(decompressed_bytes)
    
    encoded_bytes = RunLengthCompressor.encode(sample_data)
    print(encoded_bytes)
    
    decoded_bytes = RunLengthCompressor.decode(encoded_bytes)
    print(decoded_bytes)