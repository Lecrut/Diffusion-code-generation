def find_difference(numbers):
    if not numbers:
        return 0
    min_val = float('inf')
    max_val = float('-inf')
    for num in numbers:
        if num < min_val:
            min_val = num
        elif num > max_val:
            max_val = num
    return max_val - min_val

if __name__ == '__main__':
    sample_numbers = [15, 23, 7, 90, 5]
    result = find_difference(sample_numbers)
    print(result)