def print_truth_table(input_combinations):
    headers = list(input_combinations[0].keys())
    values = [list(comb.values()) for comb in input_combinations]
    print(' | '.join(headers))
    print('-' * (len(headers) * 10 - len(headers) + 1))
    for row in zip(*values):
        print(' | '.join(map(str, row)))
if __name__ == '__main__':
    input_combinations = [{'A': True, 'B': False, 'C': True}, {'A': False, 'B': True, 'C': False}, {'A': True, 'B': True, 'C': False}]
    print_truth_table(input_combinations)