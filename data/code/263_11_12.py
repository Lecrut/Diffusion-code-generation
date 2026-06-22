def find_min_max(numbers):
    min_val = numbers[0]
    max_val = numbers[0]
    for num in numbers:
        if num < min_val:
            min_val = num
        elif num > max_val:
            max_val = num
    return (min_val, max_val)
if __name__ == '__main__':
    sample_values = [34, 7, 23, 100, -5, 6]
    result = find_min_max(sample_values)
    print(result)