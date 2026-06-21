def run_length_encode(integers):
    if not integers:
        return []
    result = []
    current_value = integers[0]
    count = 1
    for value in integers[1:]:
        if value == current_value:
            count += 1
        else:
            result.append((current_value, count))
            current_value = value
            count = 1
    result.append((current_value, count))
    return result

if __name__ == '__main__':
    sample_data = [1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5, 5]
    encoded = run_length_encode(sample_data)
    print(encoded)