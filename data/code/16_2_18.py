def run_length_encode(data):
    if not data:
        return []

    result = []
    current_value = data[0]
    count = 1

    for i in range(1, len(data)):
        if data[i] == current_value:
            count += 1
        else:
            result.append((current_value, count))
            current_value = data[i]
            count = 1

    result.append((current_value, count))
    return result

if __name__ == '__main__':
    sample_data = b'\x00\x00\x00\x01\x01\x02\x02\x02\x02\x03'
    encoded = run_length_encode(sample_data)
    print(encoded)