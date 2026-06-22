def run_length_encode(data):
    if not data:
        return bytearray()
    result = bytearray()
    current = data[0]
    count = 1
    for i in range(1, len(data)):
        if data[i] == current and count < 255:
            count += 1
        else:
            result.append(count)
            result.append(current)
            current = data[i]
            count = 1
    result.append(count)
    result.append(current)
    return result

def run_length_decode(encoded):
    if not encoded:
        return bytearray()
    result = bytearray()
    i = 0
    while i < len(encoded):
        count = encoded[i]
        value = encoded[i + 1]
        result.extend(bytearray([value] * count))
        i += 2
    return result

if __name__ == '__main__':
    sample_data = bytearray([65, 65, 65, 66, 66, 67, 67, 67, 67, 68])
    encoded = run_length_encode(sample_data)
    print(encoded)
    decoded = run_length_decode(encoded)
    print(decoded)