def run_length_encode(data: bytes) -> list:
    if not data:
        return []
    encoded = []
    current_byte = data[0]
    count = 1
    for i in range(1, len(data)):
        if data[i] == current_byte and count < 255:
            count += 1
        else:
            encoded.append((current_byte, count))
            current_byte = data[i]
            count = 1
    encoded.append((current_byte, count))
    return encoded

if __name__ == '__main__':
    sample_sequence = bytes([255, 255, 0, 0, 0, 1, 1, 1, 1, 1, 128, 128])
    result = run_length_encode(sample_sequence)
    print(result)