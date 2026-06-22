def find_minimum(numbers):
    if not numbers:
        return None
    min_value = numbers[0]
    for i in range(1, len(numbers)):
        if numbers[i] < min_value:
            min_value = numbers[i]
    return min_value

if __name__ == '__main__':
    sample_data = [34, 12, 56, 8, 99, 23, 4, 78]
    result = find_minimum(sample_data)
    print(result)