def find_minimum(numbers):
    if not numbers:
        raise ValueError("The list is empty")
    min_val = numbers[0]
    for num in numbers:
        if num < min_val:
            min_val = num
    return min_val

if __name__ == '__main__':
    sample_data = [45, 12, 88, 3, 67, 29, 55, 101, 2, 76]
    result = find_minimum(sample_data)
    print(result)