def find_min(numbers):
    if not numbers:
        raise ValueError("List is empty")
    min_val = numbers[0]
    for i in range(1, len(numbers)):
        if numbers[i] < min_val:
            min_val = numbers[i]
    return min_val

if __name__ == '__main__':
    sample_numbers = [42, 17, 89, 3, 56, 23, 7, 91, 14, 38]
    result = find_min(sample_numbers)
    print(result)