def group_integers_by_remainder(int_list):
    grouped = {}
    for number in int_list:
        remainder = number % 3
        if remainder not in grouped:
            grouped[remainder] = []
        grouped[remainder].append(number)
    return grouped

if __name__ == '__main__':
    sample_numbers = [10, 23, 45, 68, 79, 91, 102]
    result = group_integers_by_remainder(sample_numbers)
    print(result)