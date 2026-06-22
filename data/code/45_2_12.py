def find_minimum(numbers):
    if not numbers:
        raise ValueError("List must not be empty")
    min_val = numbers[0]
    for num in numbers[1:]:
        if num < min_val:
            min_val = num
    return min_val

if __name__ == '__main__':
    sample_lists = [
        [3.5, 1.2, 4.8, 2.1],
        [0.0, -1.5, 2.3],
        [5.0],
    ]
    for lst in sample_lists:
        print(find_minimum(lst))
    try:
        find_minimum([])
    except ValueError as e:
        print(repr(e))