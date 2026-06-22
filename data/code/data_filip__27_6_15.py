def rle_encode(data: bytes) -> list:
    if not data:
        return []
    result = []
    count = 1
    current_byte = data[0]
    for i in range(1, len(data)):
        next_byte = data[i]
        if next_byte == current_byte and count < 255:
            count += 1
        else:
            result.append((current_byte, count))
            current_byte = next_byte
            count = 1
    result.append((current_byte, count))
    return result

if __name__ == '__main__':
    sample_data = b'WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW'
    encoded = rle_encode(sample_data)
    print(encoded)