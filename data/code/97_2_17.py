def print_truth_table(input_combinations):
    headers = input_combinations[0]
    values = input_combinations[1:]
    print(' | '.join(headers))
    print('-' * (len(headers) * 8 - len(headers) + 2))
    for row in values:
        print(' | '.join((str(val).center(6) for val in row)))
if __name__ == '__main__':
    input_combinations = [['A', 'B', 'C'], [True, True, False], [False, True, True], [True, False, True]]
    print_truth_table(input_combinations)