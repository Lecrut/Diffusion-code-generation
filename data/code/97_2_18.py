def print_truth_table(input_combinations):
    headers = input_combinations[0].keys()
    values = [list(inputs.values()) for inputs in input_combinations]
    print(' | '.join(headers))
    print('-' * (len(headers) * 12 - len(headers) + 1))
    for row in zip(*values):
        print(' | '.join((str(cell) for cell in row)))
if __name__ == '__main__':
    input_combinations = [{'A': True, 'B': False}, {'A': False, 'B': True}, {'A': True, 'B': True}, {'A': False, 'B': False}]
    print_truth_table(input_combinations)