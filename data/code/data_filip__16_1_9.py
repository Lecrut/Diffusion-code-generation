def run_length_encode(data):
    if not data:
        return []
    result = []
    current_value = data[0]
    count = 1
    for value in data[1:]:
        if value == current_value:
            count += 1
        else:
            result.append((count, current_value))
            current_value = value
            count = 1
    result.append((count, current_value))
    return result

if __name__ == '__main__':
    sample_list = [1, 1, 2, 2, 2, 3, 4, 4, 4, 4]
    encoded = run_length_encode(sample_list)
    print(encoded)