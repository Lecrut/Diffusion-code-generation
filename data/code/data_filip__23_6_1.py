def encode_rle(data: bytes) -> bytearray:
    if not data:
        return bytearray()
    
    result = bytearray()
    current_byte = data[0]
    count = 1
    length = len(data)
    
    for i in range(1, length):
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

def decode_rle(encoded: bytes) -> bytes:
    if not encoded:
        return bytes()
    
    result = bytearray()
    length = len(encoded)
    for i in range(0, length, 2):
        count = encoded[i]
        byte = encoded[i + 1]
        result.extend([byte] * count)
    
    return bytes(result)

if __name__ == '__main__':
    sample_data = b'AAAABBBCCCCCCCDDDDDDDDDDDDDDDDDDDDDDDDDDEEEEEEEEEEEEEEEEEEEEEEEE'
    encoded = encode_rle(sample_data)
    decoded = decode_rle(bytes(encoded))
    print(f"Original: {sample_data}")
    print(f"Encoded: {list(encoded)}")
    print(f"Decoded: {decoded}")
    print(f"Match: {sample_data == decoded}")