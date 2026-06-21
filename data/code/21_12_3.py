def run_length_encode(data: bytes) -> bytes:
    if not data:
        return b''
    
    result = bytearray()
    i = 0
    n = len(data)
    
    while i < n:
        current_byte = data[i]
        count = 1
        while i + count < n and data[i + count] == current_byte and count < 255:
            count += 1
        
        result.append(count)
        result.append(current_byte)
        
        i += count
    
    return bytes(result)

if __name__ == '__main__':
    sample1 = b'AAABBBCCCD'
    print(run_length_encode(sample1))
    
    sample2 = b'\x00\x00\x00\x01\x01\x02'
    print(run_length_encode(sample2))
    
    sample3 = b'ABCDEF'
    print(run_length_encode(sample3))
    
    sample4 = b''
    print(run_length_encode(sample4))
    
    sample5 = b'AAAAAAAAAAAAAAAAAAAAAAAAAA'
    print(run_length_encode(sample5))