def apply_rle(values):
    if not values:
        return []
    result = []
    current_count = 1
    current_value = values[0]
    for i in range(1, len(values)):
        if values[i] == current_value:
            current_count += 1
        else:
            result.append([current_count, current_value])
            current_value = values[i]
            current_count = 1
    result.append([current_count, current_value])
    return result

if __name__ == '__main__':
    sample_data = [1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 4]
    encoded = apply_rle(sample_data)
    print(encoded)