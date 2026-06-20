def print_truth_table(input_combinations):
    headers = input_combinations[0].keys()
    values = list(zip(*input_combinations))
    print(' | '.join(headers))
    print('-' * (len(headers) * 10 - len(headers) + 2))
    for row in zip(*values):
        print(' | '.join((str(val) for val in row)))
if __name__ == '__main__':
    input_combinations = [{'A': True, 'B': False}, {'A': False, 'B': True}, {'A': True, 'B': True}]
    print_truth_table(input_combinations)