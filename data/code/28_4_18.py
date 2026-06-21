def run_length_encode(values):
    result = []
    if not values:
        return result
    current_value = values[0]
    count = 1
    for i in range(1, len(values)):
        if values[i] == current_value:
            count += 1
        else:
            result.append((current_value, count))
            current_value = values[i]
            count = 1
    result.append((current_value, count))
    return result

if __name__ == '__main__':
    sample_data = [1, 1, 1, 2, 3, 3, 2, 2, 2, 2]
    encoded = run_length_encode(sample_data)
    print(encoded)