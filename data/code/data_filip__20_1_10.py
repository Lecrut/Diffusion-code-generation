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
    sample_data = [1, 1, 1, 2, 2, 3, 4, 4, 4, 4, 5]
    result = run_length_encode(sample_data)
    print(result)