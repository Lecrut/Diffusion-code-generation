def run_length_encode(data: bytes) -> bytes:
    if not data:
        return b""
    
    result = bytearray()
    count = 1
    current_byte = data[0]
    
    for i in range(1, len(data)):
        if data[i] == current_byte:
            count += 1
            if count == 255:
                result.append(count)
                result.append(current_byte)
                count = 0
        else:
            result.append(count)
            result.append(current_byte)
            count = 1
            current_byte = data[i]
    
    result.append(count)
    result.append(current_byte)
    
    return bytes(result)

def run_length_decode(data: bytes) -> bytes:
    if not data:
        return b""
    
    result = bytearray()
    i = 0
    while i < len(data):
        count = data[i]
        byte_value = data[i + 1]
        result.extend([byte_value] * count)
        i += 2
    
    return bytes(result)

if __name__ == '__main__':
    original = b'AABBBCCCC'
    encoded = run_length_encode(original)
    decoded = run_length_decode(encoded)
    print(encoded)
    print(decoded)