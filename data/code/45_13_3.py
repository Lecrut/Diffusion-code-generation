def find_minimum(numbers):
    if not numbers:
        return None
    current_min = numbers[0]
    for num in numbers:
        if num < current_min:
            current_min = num
    return current_min

if __name__ == '__main__':
    sample_list = [5, 2, 9, 1, 7, 3]
    result = find_minimum(sample_list)
    print(result)