def run_length_encode(data: bytes) -> bytes:
    if not data:
        return b""
    
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
    sample_data = b"AAABBBCCCDDEEEEEFFFF"
    encoded = run_length_encode(sample_data)
    print(encoded)
    
    another_sample = b"\x00\x00\x00\x01\x01\x02"
    encoded2 = run_length_encode(another_sample)
    print(encoded2)
    
    empty_sample = b""
    encoded3 = run_length_encode(empty_sample)
    print(encoded3)
    
    single_byte = b"X"
    encoded4 = run_length_encode(single_byte)
    print(encoded4)
    
    repeated_256 = b"A" * 300
    encoded5 = run_length_encode(repeated_256)
    print(encoded5)