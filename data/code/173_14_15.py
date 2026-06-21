def group_by_remainder(numbers):
    remainder_groups = {}
    for num in numbers:
        remainder = num % 3
        if remainder not in remainder_groups:
            remainder_groups[remainder] = []
        remainder_groups[remainder].append(num)
    return remainder_groups

if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    result = group_by_remainder(sample_numbers)
    print(result)