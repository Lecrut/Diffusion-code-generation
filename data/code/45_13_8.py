def find_minimum(numbers):
    if not numbers:
        raise ValueError("List cannot be empty")
    min_val = numbers[0]
    for num in numbers:
        if num < min_val:
            min_val = num
    return min_val

if __name__ == '__main__':
    sample_list = [10, -5, 3, 42, 0, -15, 25]
    result = find_minimum(sample_list)
    print(result)