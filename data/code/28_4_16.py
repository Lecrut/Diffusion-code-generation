def run_length_encode(numbers):
    if not numbers:
        return []
    result = []
    current_value = numbers[0]
    count = 1
    for i in range(1, len(numbers)):
        if numbers[i] == current_value:
            count += 1
        else:
            result.append((current_value, count))
            current_value = numbers[i]
            count = 1
    result.append((current_value, count))
    return result

if __name__ == '__main__':
    sample_data = [1, 1, 1, 2, 3, 3, 2, 2, 2, 2]
    encoded_result = run_length_encode(sample_data)
    print(encoded_result)