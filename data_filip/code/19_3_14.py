def run_length_encode(data: bytes) -> bytes:
    if not data:
        return b""
    
    result = bytearray()
    count = 1
    current_byte = data[0]
    
    for i in range(1, len(data)):
        if data[i] == current_byte:
            count += 1
        else:
            result.append(count)
            result.append(current_byte)
            count = 1
            current_byte = data[i]
    
    result.append(count)
    result.append(current_byte)
    
    return bytes(result)

if __name__ == '__main__':
    sample_data = b"AABBBCCCC"
    encoded = run_length_encode(sample_data)
    print(encoded)