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
            result.append((current_value, count))
            current_value = value
            count = 1
    result.append((current_value, count))
    return result

def run_length_decode(data):
    result = []
    for value, count in data:
        result.extend([value] * count)
    return result

if __name__ == '__main__':
    sample_list = [1, 1, 1, 2, 2, 3, 3, 3, 3, 5, 5, 5, 5, 5, 7]
    encoded = run_length_encode(sample_list)
    decoded = run_length_decode(encoded)
    print(encoded)
    print(decoded)