def run_length_encode(values):
    if not values:
        return []
    result = []
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
    sample_values = [1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5, 5, 5, 5, 5]
    print(run_length_encode(sample_values))