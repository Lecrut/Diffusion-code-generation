def find_minimum(numbers):
    if not numbers:
        raise ValueError("List cannot be empty")
    minimum = numbers[0]
    for i in range(1, len(numbers)):
        if numbers[i] < minimum:
            minimum = numbers[i]
    return minimum

if __name__ == '__main__':
    sample_data = [5, 2, 9, 1, 7, 6, 3]
    result = find_minimum(sample_data)
    print(result)