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
            encoded.append((count, current_value))
            current_value = value
            count = 1
    encoded.append((count, current_value))
    return encoded

if __name__ == '__main__':
    sample_input = [1, 1, 1, 2, 2, 3, 3, 3, 3, 5]
    print(run_length_encode(sample_input))