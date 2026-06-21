def group_integers_by_remainder(integer_list):
    grouped = {0: [], 1: [], 2: []}
    for num in integer_list:
        remainder = num % 3
        grouped[remainder].append(num)
    return grouped

if __name__ == '__main__':
    sample_integers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    result = group_integers_by_remainder(sample_integers)
    print(result)