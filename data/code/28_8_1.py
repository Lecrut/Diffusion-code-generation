def run_length_encode(data):
    if not data:
        return []

    encoded = []
    current_value = data[0]
    count = 1

    for i in range(1, len(data)):
        if data[i] == current_value:
            count += 1
        else:
            encoded.append((current_value, count))
            current_value = data[i]
            count = 1

    encoded.append((current_value, count))
    return encoded

if __name__ == '__main__':
    sample_data = [1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5, 5, 5]
    result = run_length_encode(sample_data)
    print(result)

    sample_data_large = [0] * 1000000 + [1] * 500000 + [2] * 250000
    result_large = run_length_encode(sample_data_large)
    print(result_large)