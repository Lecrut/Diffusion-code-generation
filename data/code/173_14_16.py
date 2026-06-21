def group_by_remainder(numbers):
    grouped = {}
    for num in numbers:
        remainder = num % 3
        if remainder not in grouped:
            grouped[remainder] = []
        grouped[remainder].append(num)
    return grouped

if __name__ == '__main__':
    sample_numbers = [10, 23, 45, 67, 89, 12, 34]
    result = group_by_remainder(sample_numbers)
    print(result)