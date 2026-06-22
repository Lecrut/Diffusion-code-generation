def rle_compress(data: bytes) -> bytes:
    if not data:
        return b""
    
    result = bytearray()
    count = 1
    current_byte = data[0]
    
    for i in range(1, len(data)):
        if data[i] == current_byte and count < 255:
            count += 1
        else:
            if count == 1:
                result.append(0)
                result.append(current_byte)
            else:
                result.append(count)
                result.append(current_byte)
            count = 1
            current_byte = data[i]
    
    if count == 1:
        result.append(0)
        result.append(current_byte)
    else:
        result.append(count)
        result.append(current_byte)
    
    return bytes(result)

if __name__ == '__main__':
    sample_input = b"AAABBBCCCC"
    compressed = rle_compress(sample_input)
    print(compressed)