def rle_encode(data: bytes) -> list:
    if not data:
        return []
    result = []
    current_byte = data[0]
    count = 1
    for byte in data[1:]:
        if byte == current_byte and count < 255:
            count += 1
        else:
            result.append((current_byte, count))
            current_byte = byte
            count = 1
    result.append((current_byte, count))
    return result

if __name__ == '__main__':
    test_data = b'AAABBBCCCAAA'
    encoded_result = rle_encode(test_data)
    print(encoded_result)