def run_length_encode(values):
    encoded = []
    if not values:
        return encoded
    current_value = values[0]
    count = 1
    for value in values[1:]:
        if value == current_value:
            count += 1
        else:
            encoded.append((current_value, count))
            current_value = value
            count = 1
    encoded.append((current_value, count))
    return encoded

if __name__ == '__main__':
    sample_data = [1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 1, 1]
    result = run_length_encode(sample_data)
    print(result)