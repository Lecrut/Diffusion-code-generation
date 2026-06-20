def opposite_truth_values(bool_list):
    return [not x for x in bool_list]

if __name__ == '__main__':
    sample_values = [True, False, True, False]
    print(opposite_truth_values(sample_values))