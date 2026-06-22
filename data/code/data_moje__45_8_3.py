def find_minimum(numbers):
    if not numbers:
        return None
    min_val = numbers[0]
    for num in numbers[1:]:
        if num < min_val:
            min_val = num
    return min_val

if __name__ == '__main__':
    sample_values = [34, 15, 88, 2, 93, 10]
    result = find_minimum(sample_values)
    print(result)