def find_minimum(numbers):
    if not numbers:
        raise ValueError("List is empty")
    min_val = numbers[0]
    for num in numbers[1:]:
        if num < min_val:
            min_val = num
    return min_val

if __name__ == '__main__':
    sample_numbers = [42, -7, 15, 0, 23, -3, 88]
    result = find_minimum(sample_numbers)
    print(result)