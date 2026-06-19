def find_max_difference(list_a, list_b):
    if not list_a or not list_b:
        return 0

    min_a = min(list_a)
    max_a = max(list_a)
    min_b = min(list_b)
    max_b = max(list_b)

    diff1 = abs(max_a - min_b)
    diff2 = abs(max_b - min_a)

    return max(diff1, diff2)

if __name__ == '__main__':
    sample_list_a = [5, 9, 3, 7]
    sample_list_b = [8, 2, 6, 4]
    result = find_max_difference(sample_list_a, sample_list_b)
    print(result)