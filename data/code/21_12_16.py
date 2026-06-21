def run_length_encode(data: bytes) -> bytearray:
    if not data:
        return bytearray()
    
    result = bytearray()
    count = 1
    current_byte = data[0]
    
    for i in range(1, len(data)):
        byte = data[i]
        if byte == current_byte and count < 255:
            count += 1
        else:
            result.append(count)
            result.append(current_byte)
            current_byte = byte
            count = 1
    
    result.append(count)
    result.append(current_byte)
    
    return result

if __name__ == '__main__':
    sample_data = b'AABBBBBBCDDDDDDD'
    encoded = run_length_encode(sample_data)
    print(encoded)