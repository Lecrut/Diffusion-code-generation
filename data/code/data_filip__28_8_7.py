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

def run_length_decode(encoded):
    result = []
    for value, count in encoded:
        result.extend([value] * count)
    return result

if __name__ == '__main__':
    sample_data = [1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5, 5, 5, 5, 5]
    compressed = run_length_encode(sample_data)
    print(compressed)
    decompressed = run_length_decode(compressed)
    print(decompressed)