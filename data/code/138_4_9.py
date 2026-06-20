def truth_table_results(bool_list1, bool_list2):
    return [
        (a & b, a | b, a ^ b)
        for a, b in zip(bool_list1, bool_list2)
    ]

if __name__ == '__main__':
    sample_bool_list1 = [True, False, True]
    sample_bool_list2 = [False, True, False]
    print(truth_table_results(sample_bool_list1, sample_bool_list2))