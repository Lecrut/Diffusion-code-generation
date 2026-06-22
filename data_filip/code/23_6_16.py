def encode_rle(data: bytes) -> bytearray:
    if len(data) == 0:
        return bytearray()
    result = bytearray()
    current_byte = data[0]
    count = 1
    limit = len(data)
    idx = 1
    while idx < limit:
        next_byte = data[idx]
        if next_byte == current_byte and count < 255:
            count += 1
        else:
            result.append(count)
            result.append(current_byte)
            current_byte = next_byte
            count = 1
        idx += 1
    result.append(count)
    result.append(current_byte)
    return result

if __name__ == '__main__':
    sample_input = b'AAABBBCCCCDDDEEEEEFFFFFGGGGHHHHHHIIIIIJ'
    encoded_output = encode_rle(sample_input)
    print(encoded_output)
    print(list(encoded_output))