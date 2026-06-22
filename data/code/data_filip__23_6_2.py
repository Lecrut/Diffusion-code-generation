import array

def run_length_encode(data: bytes) -> bytearray:
    encoded = bytearray()
    length = len(data)
    if length == 0:
        return encoded
    
    current_byte = data[0]
    count = 1
    
    for i in range(1, length):
        byte_val = data[i]
        if byte_val == current_byte and count < 255:
            count += 1
        else:
            encoded.append(current_byte)
            encoded.append(count)
            current_byte = byte_val
            count = 1
    
    encoded.append(current_byte)
    encoded.append(count)
    
    return encoded

def run_length_decode(data: bytearray) -> bytearray:
    decoded = bytearray()
    length = len(data)
    i = 0
    while i < length:
        if i + 1 >= length:
            break
        value = data[i]
        count = data[i + 1]
        decoded.extend([value] * count)
        i += 2
    return decoded

if __name__ == '__main__':
    original = b"AAAABBBCCDAA"
    encoded = run_length_encode(original)
    decoded = run_length_decode(encoded)
    print(encoded)
    print(decoded)