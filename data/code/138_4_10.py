def truth_table(bool_list1, bool_list2):
    return [
        (a, b, a and b, a or b, a != b)
        for a, b in zip(bool_list1, bool_list2)
    ]

if __name__ == '__main__':
    sample_values = [True, False], [False, True]
    print(truth_table(*sample_values))