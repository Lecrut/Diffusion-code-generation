def encode_run_length(data):
    if not data:
        return []
    result = []
    current_value = data[0]
    current_count = 1
    for i in range(1, len(data)):
        if data[i] == current_value:
            current_count += 1
        else:
            result.append([current_value, current_count])
            current_value = data[i]
            current_count = 1
    result.append([current_value, current_count])
    return result

if __name__ == '__main__':
    sample_input = [1, 1, 1, 2, 2, 3, 3, 3, 3, 5]
    encoded_result = encode_run_length(sample_input)
    print(encoded_result)