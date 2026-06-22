def find_minimum(numbers):
    if not numbers:
        return None
    min_val = numbers[0]
    for num in numbers:
        if num < min_val:
            min_val = num
    return min_val

if __name__ == '__main__':
    sample_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
    result = find_minimum(sample_numbers)
    print(result)