import ctypes

def rle_encode(data: bytes) -> bytes:
    if not data:
        return b""
    length = len(data)
    if length == 0:
        return b""
    
    result = bytearray()
    i = 0
    while i < length:
        current_byte = data[i]
        count = 1
        while i + count < length and data[i + count] == current_byte:
            count += 1
        
        if count == 1:
            result.append(0)
            result.append(current_byte)
        else:
            result.append(count)
            result.append(current_byte)
        i += count
    
    return bytes(result)

def rle_decode(data: bytes) -> bytes:
    if not data:
        return b""
    length = len(data)
    if length == 0:
        return b""
    
    result = bytearray()
    i = 0
    while i < length:
        count = data[i]
        i += 1
        if i >= length:
            break
        byte_val = data[i]
        i += 1
        
        if count == 0:
            result.append(byte_val)
        else:
            result.extend([byte_val] * count)
            
    return bytes(result)

if __name__ == '__main__':
    sample_data = b"AAABBBCCCC"
    encoded = rle_encode(sample_data)
    decoded = rle_decode(encoded)
    print(f"Original: {sample_data}")
    print(f"Encoded:  {encoded}")
    print(f"Decoded:  {decoded}")
    print(f"Match:    {sample_data == decoded}")