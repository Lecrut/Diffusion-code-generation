def run_length_encode(numbers):
    if not numbers:
        return []
    encoded = []
    current_count = 1
    current_value = numbers[0]
    for i in range(1, len(numbers)):
        if numbers[i] == current_value:
            current_count += 1
        else:
            encoded.append([current_count, current_value])
            current_value = numbers[i]
            current_count = 1
    encoded.append([current_count, current_value])
    return encoded

if __name__ == '__main__':
    sample_data = [1, 1, 2, 2, 2, 3, 3, 1, 1, 1, 1, 5]
    result = run_length_encode(sample_data)
    print(result)