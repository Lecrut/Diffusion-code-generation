def find_min_max_bitwise(numbers):
    if not numbers:
        return (None, None)
    min_val = max_val = numbers[0]
    for num in numbers[1:]:
        min_val = min_val & ~((min_val ^ num) >> 31) | num & (min_val ^ num) >> 31
        max_val = max_val & ~((max_val ^ num) >> 31) | num & ~(max_val ^ num) >> 31
    return (min_val, max_val)
if __name__ == '__main__':
    sample_values = [3, 5, 1, 8, -2, 7]
    print(find_min_max_bitwise(sample_values))