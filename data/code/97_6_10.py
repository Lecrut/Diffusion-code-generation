def print_truth_table(input_tuples):
    headers = ['P', 'Q', 'P AND Q', 'P OR Q', 'NOT P', 'NOT Q']
    print(' | '.join(headers))
    for p, q in input_tuples:
        and_result = p and q
        or_result = p or q
        not_p = not p
        not_q = not q
        row = [str(p), str(q), str(and_result), str(or_result), str(not_p), str(not_q)]
        print(' | '.join(row))

if __name__ == '__main__':
    sample_values = [(True, True), (True, False), (False, True), (False, False)]
    print_truth_table(sample_values)