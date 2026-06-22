def find_minimum(numbers):
    if not numbers:
        raise ValueError("List is empty")
    min_val = numbers[0]
    for num in numbers[1:]:
        if num < min_val:
            min_val = num
    return min_val

if __name__ == '__main__':
    sample_list = [34, 15, 88, 2, 79, 45, -10, 3, 99, 0]
    result = find_minimum(sample_list)
    print(result)