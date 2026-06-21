def run_length_encode(data: bytes) -> bytes:
    if not data:
        return b''
    result = bytearray()
    count = 1
    length = len(data)
    prev_byte = data[0]
    for i in range(1, length):
        current_byte = data[i]
        if current_byte == prev_byte and count < 255:
            count += 1
        else:
            result.append(count)
            result.append(prev_byte)
            count = 1
            prev_byte = current_byte
    result.append(count)
    result.append(prev_byte)
    return bytes(result)

if __name__ == '__main__':
    sample_data = b'WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB'
    encoded = run_length_encode(sample_data)
    print(encoded)