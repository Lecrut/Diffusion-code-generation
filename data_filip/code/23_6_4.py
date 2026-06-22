class RLEEncoder:
    def __init__(self, data: bytes):
        self.data = data
        self.length = len(data)

    def encode(self) -> bytes:
        if self.length == 0:
            return b''
        
        data = self.data
        result = bytearray()
        
        current_byte = data[0]
        count = 1
        
        for i in range(1, self.length):
            byte_val = data[i]
            if byte_val == current_byte and count < 255:
                count += 1
            else:
                result.append(current_byte)
                result.append(count)
                current_byte = byte_val
                count = 1
        
        result.append(current_byte)
        result.append(count)
        
        return bytes(result)

if __name__ == '__main__':
    sample_data = b'AAAABBBCCDAA'
    encoder = RLEEncoder(sample_data)
    encoded_result = encoder.encode()
    print(encoded_result)