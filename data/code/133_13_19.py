TRUTH_VALUES = {'True': True, 'False': False}

def evaluate_truth_values(bool_list):
    return [str(b).capitalize() for b in bool_list]

if __name__ == '__main__':
    sample_values = [True, False, True, False]
    print(evaluate_truth_values(sample_values))