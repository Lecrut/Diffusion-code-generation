def find_minimum(numbers):
    if not numbers:
        return None
    min_val = numbers[0]
    for num in numbers:
        if num < min_val:
            min_val = num
    return min_val

if __name__ == '__main__':
    sample_list = [42, -7, 15, 0, 23, -19, 8]
    result = find_minimum(sample_list)
    print(result)