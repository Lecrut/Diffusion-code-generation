def run_length_encode(numbers):
    encoded = []
    if not numbers:
        return encoded

    current_value = numbers[0]
    count = 1

    for value in numbers[1:]:
        if value == current_value:
            count += 1
        else:
            encoded.append((current_value, count))
            current_value = value
            count = 1

    encoded.append((current_value, count))
    return encoded

if __name__ == '__main__':
    sample_data = [1, 1, 2, 3, 3, 3, 4, 4, 4, 4]
    result = run_length_encode(sample_data)
    print(result)