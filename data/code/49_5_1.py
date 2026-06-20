def compare_lengths(len1, len2):
    if len1 == len2:
        return 'equal'
    elif len1 > len2:
        return 'len1 is greater'
    else:
        return 'len2 is greater'

if __name__ == '__main__':
    length_a = 10
    length_b = 5
    result_a = compare_lengths(length_a, length_b)
    print(result_a)
    length_c = 3
    length_d = 7
    result_b = compare_lengths(length_c, length_d)
    print(result_b)
    length_e = 4
    length_f = 4
    result_c = compare_lengths(length_e, length_f)
    print(result_c)