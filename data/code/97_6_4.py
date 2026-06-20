def print_truth_table(input_tuples):
    headers = ['P', 'Q', 'P or Q']
    truth_values = {'True': 1, 'False': 0}
    print(' | '.join(headers))
    print('-' * (len(headers) * 8 - 3))
    for P, Q in input_tuples:
        result = truth_values[P] or truth_values[Q]
        print(f'{P} | {Q} | {('True' if result else 'False')}')
if __name__ == '__main__':
    sample_inputs = [('True', 'True'), ('True', 'False'), ('False', 'True'), ('False', 'False')]
    print_truth_table(sample_inputs)