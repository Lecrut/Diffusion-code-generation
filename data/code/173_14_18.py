def group_integers_by_remainder(integer_list):
    grouped_dict = {}
    remainder_threshold = 3
    for num in integer_list:
        remainder = num % remainder_threshold
        if remainder not in grouped_dict:
            grouped_dict[remainder] = []
        grouped_dict[remainder].append(num)
    return grouped_dict

if __name__ == '__main__':
    sample_integers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    result = group_integers_by_remainder(sample_integers)
    print(result)