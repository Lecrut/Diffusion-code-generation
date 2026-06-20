def print_truth_table(tuples):
    headers = ('P', 'Q', 'P∧Q', 'P∨Q', '¬P', '¬Q')
    print(' | '.join(headers))
    for p, q in tuples:
        print(f'{p} | {q} | {p and q} | {p or q} | {not p} | {not q}')

if __name__ == '__main__':
    sample_values = [(True, True), (True, False), (False, True), (False, False)]
    print_truth_table(sample_values)