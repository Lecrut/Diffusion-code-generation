def run_length_encode(numbers):
    if not numbers:
        return []
    result = []
    current_count = 1
    current_value = numbers[0]
    for i in range(1, len(numbers)):
        if numbers[i] == current_value:
            current_count += 1
        else:
            result.append([current_count, current_value])
            current_value = numbers[i]
            current_count = 1
    result.append([current_count, current_value])
    return result

if __name__ == '__main__':
    sample_input = [1, 1, 2, 3, 3, 3, 4, 4]
    print(run_length_encode(sample_input))
    print(run_length_encode([]))