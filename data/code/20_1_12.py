def run_length_encode(data):
    if not data:
        return []
    encoded = []
    current_val = data[0]
    count = 1
    for i in range(1, len(data)):
        if data[i] == current_val:
            count += 1
        else:
            encoded.append((current_val, count))
            current_val = data[i]
            count = 1
    encoded.append((current_val, count))
    return encoded

if __name__ == '__main__':
    sample_list = [1, 1, 1, 2, 2, 3, 3, 3, 3, 5, 7, 7, 7]
    result = run_length_encode(sample_list)
    print(result)