def find_minimum(numbers):
    if not numbers:
        raise ValueError("Cannot find minimum of an empty list")
    min_val = numbers[0]
    for num in numbers[1:]:
        if num < min_val:
            min_val = num
    return min_val

if __name__ == '__main__':
    sample_list = [5, 2, 9, 1, 7, 3]
    result = find_minimum(sample_list)
    print(result)