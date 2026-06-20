def print_truth_table(input_tuples):
    headers = ['P', 'Q', 'P AND Q', 'P OR Q', 'NOT P', 'NOT Q']
    print(' | '.join(headers))
    for p, q in input_tuples:
        print(f'{p} | {q} | {p and q} | {p or q} | {not p} | {not q}')

if __name__ == '__main__':
    sample_values = [(True, True), (True, False), (False, True), (False, False)]
    print_truth_table(sample_values)