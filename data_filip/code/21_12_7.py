def run_length_encode(data: bytes) -> bytes:
    if not data:
        return b""
    
    result = bytearray()
    count = 1
    current_byte = data[0]
    length = len(data)
    
    i = 1
    while i < length:
        byte = data[i]
        if byte == current_byte and count < 255:
            count += 1
        else:
            result.append(count)
            result.append(current_byte)
            current_byte = byte
            count = 1
        i += 1
        
    result.append(count)
    result.append(current_byte)
    
    return bytes(result)

def run_length_decode(data: bytes) -> bytes:
    if not data:
        return b""
    
    length = len(data)
    if length % 2 != 0:
        raise ValueError("Encoded data must have even length")
    
    result = bytearray()
    
    i = 0
    while i < length:
        count = data[i]
        byte = data[i + 1]
        result.extend(bytes([byte]) * count)
        i += 2
        
    return bytes(result)

if __name__ == '__main__':
    original = b"AAAABBBCCDAA"
    encoded = run_length_encode(original)
    decoded = run_length_decode(encoded)
    
    print(f"Original: {original}")
    print(f"Encoded: {encoded}")
    print(f"Decoded: {decoded}")
    print(f"Match: {original == decoded}")