def run_length_encode(data):
    if not data:
        return []
    result = []
    current_val = data[0]
    count = 1
    for i in range(1, len(data)):
        if data[i] == current_val:
            count += 1
        else:
            result.append((current_val, count))
            current_val = data[i]
            count = 1
    result.append((current_val, count))
    return result

if __name__ == '__main__':
    sample_data = [1, 1, 1, 2, 3, 3, 4, 4, 4, 4]
    encoded = run_length_encode(sample_data)
    print(encoded)