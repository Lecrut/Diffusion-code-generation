def run_length_encode(data):
    if not data:
        return b''
    result = bytearray()
    current_byte = data[0]
    count = 1
    for i in range(1, len(data)):
        byte = data[i]
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

if __name__ == '__main__':
    sample_data = bytes([0, 0, 0, 1, 1, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 5])
    encoded = run_length_encode(sample_data)
    print(list(encoded))
    decoded_list = []
    for i in range(0, len(encoded), 2):
        count = encoded[i]
        value = encoded[i + 1]
        decoded_list.extend([value] * count)
    print(decoded_list)
    print(list(sample_data) == decoded_list)