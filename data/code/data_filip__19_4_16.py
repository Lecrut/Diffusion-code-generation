def run_length_encode(data):
    if not data:
        return []
    result = []
    count = 1
    current_value = data[0]
    for i in range(1, len(data)):
        if data[i] == current_value:
            count += 1
        else:
            result.append([count, current_value])
            current_value = data[i]
            count = 1
    result.append([count, current_value])
    return result

if __name__ == '__main__':
    sample_data = [1, 1, 1, 2, 3, 3, 2, 2]
    encoded = run_length_encode(sample_data)
    print(encoded)
    empty_result = run_length_encode([])
    print(empty_result)