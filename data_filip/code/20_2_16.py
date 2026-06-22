def compress_rle(data: bytes) -> bytes:
    if not data:
        return b''
    
    result = []
    current_byte = data[0]
    count = 1
    
    for i in range(1, len(data)):
        if data[i] == current_byte and count < 255:
            count += 1
        else:
            result.append(bytes([count, current_byte]))
            current_byte = data[i]
            count = 1
    
    result.append(bytes([count, current_byte]))
    return b''.join(result)

if __name__ == '__main__':
    sample_data = b'\x00\x00\x00\x00\xFF\xFF\xFF\x41\x41\x42'
    compressed = compress_rle(sample_data)
    print(compressed.hex())