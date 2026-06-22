def find_minimum(numbers):
    if not numbers:
        raise ValueError("The list is empty")

    min_val = numbers[0]

    for i in range(1, len(numbers)):
        if numbers[i] < min_val:
            min_val = numbers[i]

    return min_val

if __name__ == '__main__':
    sample_list = [34, 15, 88, 2, 90, 23, 7]
    result = find_minimum(sample_list)
    print(result)