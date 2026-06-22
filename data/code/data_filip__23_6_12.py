def run_length_encode(data: bytes) -> bytearray:
    if not data:
        return bytearray()

    result = bytearray()
    length = len(data)
    i = 0

    while i < length:
        current_byte = data[i]
        count = 1
        next_i = i + 1

        while next_i < length and data[next_i] == current_byte:
            count += 1
            next_i += 1

        if count < 128:
            result.append(count)
            result.append(current_byte)
        else:
            while count >= 255:
                result.append(255)
                result.append(current_byte)
                count -= 255
            result.append(count)
            result.append(current_byte)

        i = next_i

    return result

def run_length_decode(data: bytearray) -> bytes:
    if not data:
        return b''

    result = bytearray()
    length = len(data)
    i = 0

    while i < length:
        count = data[i]
        value = data[i + 1]
        result.extend([value] * count)
        i += 2

    return bytes(result)

if __name__ == '__main__':
    original_data = bytes([65, 65, 65, 66, 67, 67, 67, 67, 67, 67, 67, 67])
    encoded = run_length_encode(original_data)
    print(encoded)
    decoded = run_length_decode(encoded)
    print(decoded)