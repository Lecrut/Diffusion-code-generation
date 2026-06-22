def find_minimum(numbers):
    if not numbers:
        raise ValueError("List must not be empty")
    min_val = numbers[0]
    for num in numbers[1:]:
        if num < min_val:
            min_val = num
    return min_val

if __name__ == '__main__':
    sample_list = [3.5, 1.2, 4.8, 2.1, 9.3]
    result = find_minimum(sample_list)
    print(result)
    empty_list = []
    try:
        find_minimum(empty_list)
    except ValueError as e:
        print(str(e))