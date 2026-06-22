def rle_encode_byte_string(data: bytes) -> bytes:
    if not data:
        return b''
    
    result = bytearray()
    current_byte = data[0]
    count = 1
    
    for i in range(1, len(data)):
        if data[i] == current_byte and count < 255:
            count += 1
        else:
            result.append(count)
            result.append(current_byte)
            current_byte = data[i]
            count = 1
            
    result.append(count)
    result.append(current_byte)
    
    return bytes(result)

if __name__ == '__main__':
    sample_data = b'AAAABBBCCDAA'
    sample_bytes = bytes([65, 65, 65, 65, 66, 66, 66, 67, 67, 68, 65, 65])
    encoded = rle_encode_byte_string(sample_bytes)
    print(encoded)