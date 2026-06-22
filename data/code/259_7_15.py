def find_min_max_bitwise(numbers):
    if not numbers:
        return (None, None)
    min_val = max_val = numbers[0]
    for num in numbers[1:]:
        min_val = num & min_val | ~num & min_val
        max_val = ~num & max_val | num & ~max_val
    return (min_val, max_val)
if __name__ == '__main__':
    sample_values = [3, 5, 1, 2, 4]
    print(find_min_max_bitwise(sample_values))