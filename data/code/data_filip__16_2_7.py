def run_length_encode(data):
    if not data:
        return []
    encoded = []
    current_byte = data[0]
    count = 1
    for i in range(1, len(data)):
        if data[i] == current_byte:
            count += 1
        else:
            encoded.append((current_byte, count))
            current_byte = data[i]
            count = 1
    encoded.append((current_byte, count))
    return encoded

if __name__ == '__main__':
    sample_data = [1, 1, 2, 3, 3, 3, 4, 4, 4, 4]
    result = run_length_encode(sample_data)
    print(result)