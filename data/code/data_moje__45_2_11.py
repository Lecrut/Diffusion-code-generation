def find_minimum(numbers):
    if not numbers:
        raise ValueError("Cannot find minimum of an empty list")
    min_val = numbers[0]
    for num in numbers[1:]:
        if num < min_val:
            min_val = num
    return min_val

if __name__ == '__main__':
    sample_list = [3.14, 1.59, 2.65, 3.58, 9.79]
    result = find_minimum(sample_list)
    print(result)