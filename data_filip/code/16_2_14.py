def run_length_encode(data):
    if not data:
        return []
    result = []
    current_byte = data[0]
    count = 1
    for i in range(1, len(data)):
        if data[i] == current_byte:
            count += 1
        else:
            result.append((current_byte, count))
            current_byte = data[i]
            count = 1
    result.append((current_byte, count))
    return result

if __name__ == '__main__':
    sample_data = bytes([72, 72, 72, 101, 108, 108, 111, 32, 32, 32, 119, 111])
    encoded_data = run_length_encode(sample_data)
    print(encoded_data)