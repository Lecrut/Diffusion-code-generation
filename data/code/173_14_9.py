def group_integers_by_remainder(int_list):
    grouped = {}
    for num in int_list:
        remainder = num % 3
        if remainder not in grouped:
            grouped[remainder] = []
        grouped[remainder].append(num)
    return grouped

if __name__ == '__main__':
    sample_ints = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    result = group_integers_by_remainder(sample_ints)
    print(result)