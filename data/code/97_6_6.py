def print_truth_table(tuples):
    headers = ['P', 'Q', 'P or Q']
    print(' | '.join(headers))
    for p, q in tuples:
        result = 'True' if p or q else 'False'
        print(f'{p} | {q} | {result}')

if __name__ == '__main__':
    sample_values = [(True, True), (True, False), (False, True), (False, False)]
    print_truth_table(sample_values)