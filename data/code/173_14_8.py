def group_integers_by_remainder(integer_list):
    grouped = {}
    for num in integer_list:
        remainder = num % 3
        if remainder not in grouped:
            grouped[remainder] = []
        grouped[remainder].append(num)
    return grouped

if __name__ == '__main__':
    sample_numbers = [10, 23, 45, 67, 89, 12, 34, 56]
    result = group_integers_by_remainder(sample_numbers)
    print(result)