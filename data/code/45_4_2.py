def find_minimum(numbers):
    if not numbers:
        raise ValueError("List is empty")
    min_val = numbers[0]
    for num in numbers[1:]:
        if num < min_val:
            min_val = num
    return min_val

if __name__ == '__main__':
    sample_values = [42, 7, 19, 3, 88, 1, 55, 23]
    result = find_minimum(sample_values)
    print(result)