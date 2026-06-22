def run_length_encode(values):
    if not values:
        return []
    encoded = []
    current_count = 1
    for i in range(1, len(values)):
        if values[i] == values[i - 1]:
            current_count += 1
        else:
            encoded.append((values[i - 1], current_count))
            current_count = 1
    encoded.append((values[-1], current_count))
    return encoded

if __name__ == '__main__':
    sample_data = [1, 1, 1, 2, 3, 3, 2, 2, 2, 2]
    result = run_length_encode(sample_data)
    print(result)