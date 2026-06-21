def rle_encode(data: bytes) -> bytes:
    if not data:
        return b""
    result = bytearray()
    n = len(data)
    i = 0
    while i < n:
        current_byte = data[i]
        count = 1
        while i + count < n and data[i + count] == current_byte and count < 255:
            count += 1
        result.append(count)
        result.append(current_byte)
        i += count
    return bytes(result)

def rle_decode(data: bytes) -> bytes:
    if not data:
        return b""
    if len(data) % 2 != 0:
        raise ValueError("Invalid RLE data: odd length")
    result = bytearray()
    n = len(data)
    i = 0
    while i < n:
        count = data[i]
        byte = data[i + 1]
        result.extend([byte] * count)
        i += 2
    return bytes(result)

if __name__ == '__main__':
    sample_input = b"WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWB"
    encoded = rle_encode(sample_input)
    decoded = rle_decode(encoded)
    print(encoded)
    print(decoded)
    print(encoded == rle_encode(decoded))