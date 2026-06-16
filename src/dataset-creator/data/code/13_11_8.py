def find_max(numbers):
    if not numbers:
        return None
    max_val = numbers[0]
    for num in numbers[1:]:
        if num > max_val:
            max_val = num
    return max_val
if __name__ == '__main__':
    sample_data = [3, 7, 2, 9, 4, -5, 0]
    result = find_max(sample_data)
    print(result)