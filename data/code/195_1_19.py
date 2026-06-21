def find_first_difference(list1, list2):
    min_len = min(len(list1), len(list2))
    for i in range(min_len):
        if list1[i] != list2[i]:
            return i
    if len(list1) != len(list2):
        return min_len
    return -1
if __name__ == '__main__':
    sample_a = [1, 2, 3, 4]
    sample_b = [1, 2, 9, 4]
    sample_c = [1, 2, 3, 4]
    result_ab = find_first_difference(sample_a, sample_b)
    result_ac = find_first_difference(sample_a, sample_c)
    print(result_ab)
    print(result_ac)