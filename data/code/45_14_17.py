def find_minimum(numbers):
    if not numbers:
        return None
    min_val = numbers[0]
    for num in numbers[1:]:
        if num < min_val:
            min_val = num
    return min_val

if __name__ == '__main__':
    sample_numbers = [5, 3, 9, 1, 7, 2]
    result = find_minimum(sample_numbers)
    print(result)