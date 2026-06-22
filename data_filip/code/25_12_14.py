def run_length_encode(data: bytes) -> bytes:
    if not data:
        return b''
    result = bytearray()
    current_byte = data[0]
    count = 1
    for byte in data[1:]:
        if byte == current_byte and count < 255:
            count += 1
        else:
            result.append(count)
            result.append(current_byte)
            current_byte = byte
            count = 1
    result.append(count)
    result.append(current_byte)
    return bytes(result)

def run_length_decode(data: bytes) -> bytes:
    if not data:
        return b''
    if len(data) % 2 != 0:
        raise ValueError("Encoded data must have even length")
    result = bytearray()
    for i in range(0, len(data), 2):
        count = data[i]
        byte = data[i + 1]
        result.extend([byte] * count)
    return bytes(result)

if __name__ == '__main__':
    sample_data = b'AAABBBCCD'
    encoded = run_length_encode(sample_data)
    decoded = run_length_decode(encoded)
    print(encoded)
    print(decoded)