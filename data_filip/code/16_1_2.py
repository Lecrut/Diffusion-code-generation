def run_length_encode(data):
    if not data:
        return []
    encoded = []
    current_value = data[0]
    count = 1
    for value in data[1:]:
        if value == current_value:
            count += 1
        else:
            encoded.append((current_value, count))
            current_value = value
            count = 1
    encoded.append((current_value, count))
    return encoded

if __name__ == '__main__':
    sample_list = [1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5, 5, 5]
    result = run_length_encode(sample_list)
    print(result)