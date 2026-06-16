def find_max_element(numbers):
    if not numbers:
        raise ValueError("Input list cannot be empty")
    max_val = numbers[0]
    for num in numbers[1:]:
        if num > max_val:
            max_val = num
    return max_val
if __name__ == '__main__':
    sample_list = [3, 7, 2, 9, 5, 4, -1]
    result = find_max_element(sample_list)
    print(result)