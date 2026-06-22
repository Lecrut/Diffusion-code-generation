def run_length_encode(data):
    if not data:
        return []
    result = []
    current_count = 1
    current_value = data[0]
    for i in range(1, len(data)):
        if data[i] == current_value:
            current_count += 1
        else:
            result.append([current_count, current_value])
            current_value = data[i]
            current_count = 1
    result.append([current_count, current_value])
    return result

if __name__ == '__main__':
    sample_input = [1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 4, 5]
    encoded_result = run_length_encode(sample_input)
    print(encoded_result)