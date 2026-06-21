def run_length_encode(data: bytes) -> bytes:
    if not data:
        return b''
    
    result = bytearray()
    i = 0
    n = len(data)
    
    while i < n:
        current_byte = data[i]
        run_length = 1
        
        while i + run_length < n and data[i + run_length] == current_byte and run_length < 127:
            run_length += 1
        
        result.append(run_length)
        result.append(current_byte)
        
        i += run_length
    
    return bytes(result)

if __name__ == '__main__':
    sample_data = b'\x00\x00\x00\x00\x00\x01\x01\x01\x02\x02\x03\x03\x03\x03\x03\x03'
    compressed = run_length_encode(sample_data)
    print(compressed)