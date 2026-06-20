def evaluate_truth_values(bool_list):
    if not all(isinstance(b, bool) for b in bool_list):
        raise ValueError("Input must be a list of boolean values.")
    return ['True' if b else 'False' for b in bool_list]

if __name__ == '__main__':
    sample_values = [True, False, True, False]
    print(evaluate_truth_values(sample_values))