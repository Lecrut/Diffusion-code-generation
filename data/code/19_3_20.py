def rle_compress(data: bytes) -> bytes:
    if not data:
        return b""
    
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
    sample_data = b"AAABBBCCCC"
    compressed = rle_compress(sample_data)
    print(compressed)