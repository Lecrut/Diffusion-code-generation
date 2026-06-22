def run_length_encode(data):
    if not data:
        return []
    encoded = []
    current = data[0]
    count = 1
    for i in range(1, len(data)):
        if data[i] == current:
            count += 1
        else:
            encoded.append((count, current))
            current = data[i]
            count = 1
    encoded.append((count, current))
    return encoded

if __name__ == '__main__':
    sample_input = [1, 1, 1, 2, 2, 3, 3, 3, 3, 5]
    result = run_length_encode(sample_input)
    print(result)