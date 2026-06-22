def run_length_encode(data: bytes) -> list:
    if not data:
        return []
    result = []
    current_value = data[0]
    count = 1
    for byte in data[1:]:
        if byte == current_value:
            count += 1
        else:
            result.append((current_value, count))
            current_value = byte
            count = 1
    result.append((current_value, count))
    return result

if __name__ == '__main__':
    sample_data = b'\x00\x00\x00\x01\x01\x02\x02\x02\x02\x03'
    encoded = run_length_encode(sample_data)
    print(encoded)