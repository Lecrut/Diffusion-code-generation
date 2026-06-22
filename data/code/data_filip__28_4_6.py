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

if __name__ == '__main__':
    sample_data = [1, 1, 1, 2, 2, 3, 3, 3, 3, 1, 1, 4, 5, 5, 5]
    print(run_length_encode(sample_data))