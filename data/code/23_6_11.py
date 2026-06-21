def run_length_encode(data):
    if not data:
        return b''
    result = bytearray()
    current = data[0]
    count = 1
    for item in data[1:]:
        if item == current and count < 255:
            count += 1
        else:
            result.append(count)
            result.append(current)
            current = item
            count = 1
    result.append(count)
    result.append(current)
    return bytes(result)

def run_length_decode(data):
    if not data:
        return b''
    result = bytearray()
    i = 0
    while i < len(data):
        count = data[i]
        value = data[i + 1]
        result.extend([value] * count)
        i += 2
    return bytes(result)

if __name__ == '__main__':
    sample_data = b'\x00\x00\x00\x00\x01\x01\x02\x03\x03\x03\x03\x03\x04\x04\x04\x04\x04'
    encoded = run_length_encode(sample_data)
    print(encoded)
    decoded = run_length_decode(encoded)
    print(decoded)