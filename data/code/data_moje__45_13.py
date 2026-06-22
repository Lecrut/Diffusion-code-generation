def find_minimum(numbers):
    if not numbers:
        return None
    min_val = numbers[0]
    for num in numbers[1:]:
        if num < min_val:
            min_val = num
    return min_val

if __name__ == '__main__':
    sample_list = [42, -7, 15, 0, 3, -22, 99, 1]
    result = find_minimum(sample_list)
    print(result)