def truth_table(boolean_list1, boolean_list2):
    return [(a and b, a or b, a != b) for a, b in zip(boolean_list1, boolean_list2)]

if __name__ == '__main__':
    sample_values = [True, False, True, False]
    print(truth_table(sample_values, sample_values))