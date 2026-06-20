def print_truth_table(tuples):
    headers = ('P', 'Q', 'P AND Q', 'P OR Q', 'NOT P', 'NOT Q')
    print(' | '.join(headers))
    for p, q in tuples:
        row = (p, q, p and q, p or q, not p, not q)
        print(' | '.join(str(val) for val in row))

if __name__ == '__main__':
    sample_values = [(True, True), (True, False), (False, True), (False, False)]
    print_truth_table(sample_values)