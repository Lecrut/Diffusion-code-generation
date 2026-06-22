def run_length_encode(data):
    result = []
    if not data:
        return result
    current_value = data[0]
    current_count = 1
    for i in range(1, len(data)):
        value = data[i]
        if value == current_value:
            current_count += 1
        else:
            result.append([current_count, current_value])
            current_value = value
            current_count = 1
    result.append([current_count, current_value])
    return result

if __name__ == '__main__':
    sample_data = [1, 1, 1, 2, 3, 3, 2, 2]
    encoded = run_length_encode(sample_data)
    print(encoded)