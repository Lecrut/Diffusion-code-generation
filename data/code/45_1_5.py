def find_minimum(numbers):
    if not numbers:
        return None

    min_val = numbers[0]

    for i in range(1, len(numbers)):
        if numbers[i] < min_val:
            min_val = numbers[i]

    return min_val

if __name__ == '__main__':
    sample_list = [34, -12, 5, 0, 27, -45, 8]
    result = find_minimum(sample_list)
    print(result)