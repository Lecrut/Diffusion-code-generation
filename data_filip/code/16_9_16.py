def run_length_encode(data, tolerance=1e-9):
    if not data:
        return []
    encoded = []
    current_val = data[0]
    count = 1
    for i in range(1, len(data)):
        if abs(data[i] - current_val) <= tolerance:
            count += 1
        else:
            encoded.append((current_val, count))
            current_val = data[i]
            count = 1
    encoded.append((current_val, count))
    return encoded

if __name__ == '__main__':
    sample_data = [1.0, 1.0, 1.0, 2.0, 2.0, 3.5, 3.5000000001, 4.0]
    result = run_length_encode(sample_data)
    print(result)