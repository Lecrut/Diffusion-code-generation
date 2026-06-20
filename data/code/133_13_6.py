def evaluate_truth_values(bool_list):
    if not all(isinstance(x, bool) for x in bool_list):
        raise ValueError("All elements must be boolean values.")
    return ['True' if b else 'False' for b in bool_list]

if __name__ == '__main__':
    sample_values = [True, False, True, False]
    print(evaluate_truth_values(sample_values))