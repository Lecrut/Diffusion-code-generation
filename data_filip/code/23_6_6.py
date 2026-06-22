def encode_rle(data: bytearray) -> bytearray:
    encoded = bytearray()
    length = len(data)
    if length == 0:
        return encoded
    current = data[0]
    count = 1
    i = 1
    while i < length:
        byte = data[i]
        if byte == current and count < 255:
            count += 1
        else:
            encoded.append(current)
            encoded.append(count)
            current = byte
            count = 1
        i += 1
    encoded.append(current)
    encoded.append(count)
    return encoded

if __name__ == '__main__':
    sample = bytearray([65, 65, 65, 66, 66, 67, 67, 67, 67])
    result = encode_rle(sample)
    print(result)