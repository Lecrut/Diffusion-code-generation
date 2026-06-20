def print_truth_table(input_combinations):
    headers = input_combinations[0].keys()
    values = list(zip(*input_combinations))
    print(' | '.join(headers))
    print('-' * (len(headers) * 10 - len(headers) + 2))
    for row in zip(*values):
        print(' | '.join((str(cell) for cell in row)))
if __name__ == '__main__':
    sample_combinations = [{'A': True, 'B': False}, {'A': False, 'B': True}, {'A': True, 'B': True}, {'A': False, 'B': False}]
    print_truth_table(sample_combinations)