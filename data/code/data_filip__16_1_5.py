def run_length_encode(data):
    if not data:
        return []
    encoded = []
    count = 1
    for i in range(1, len(data)):
        if data[i] == data[i - 1]:
            count += 1
        else:
            encoded.append((data[i - 1], count))
            count = 1
    encoded.append((data[-1], count))
    return encoded

if __name__ == '__main__':
    sample_input = [1, 1, 1, 2, 3, 3, 3, 3, 4]
    result = run_length_encode(sample_input)
    print(result)