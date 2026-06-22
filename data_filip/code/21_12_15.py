def run_length_encode(data: bytes) -> bytearray:
    if not data:
        return bytearray()
    
    result = bytearray()
    length = len(data)
    i = 0
    
    while i < length:
        current_byte = data[i]
        count = 1
        
        while i + count < length and data[i + count] == current_byte and count < 255:
            count += 1
        
        result.append(count)
        result.append(current_byte)
        i += count
    
    return result

if __name__ == '__main__':
    sample_data = b'WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW'
    encoded = run_length_encode(sample_data)
    print(list(encoded))