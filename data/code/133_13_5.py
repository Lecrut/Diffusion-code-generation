def evaluate_truth_values(bool_list):
    return ['True' if x else 'False' for x in bool_list]

if __name__ == '__main__':
    sample_values = [True, False, True, False]
    print(evaluate_truth_values(sample_values))