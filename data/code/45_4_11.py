def find_minimum(numbers):
    min_val = numbers[0]
    for num in numbers:
        if num < min_val:
            min_val = num
    return min_val

if __name__ == '__main__':
    sample_data = [34, -10, 42, 0, 99, -5, 15]
    result = find_minimum(sample_data)
    print(result)