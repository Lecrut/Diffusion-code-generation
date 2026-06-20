def print_truth_table(input_tuples):
    headers = ['P', 'Q', 'P or Q']
    print(' | '.join(headers))
    for p, q in input_tuples:
        result = p or q
        print(f'{p} | {q} | {result}')

if __name__ == '__main__':
    sample_values = [(True, True), (True, False), (False, True), (False, False)]
    print_truth_table(sample_values)