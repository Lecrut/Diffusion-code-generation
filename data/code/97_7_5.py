import itertools
def print_truth_table(input_tuples):
    if not input_tuples:
        return
    p_values = [t[0] for t in input_tuples]
    q_values = [t[1] for t in input_tuples]
    header = "P | Q | P AND Q | P OR Q | NOT P"
    print("-" * len(header))
    print(header)
    print("-" * len(header))
    for p, q in itertools.product(['T', 'F'], repeat=2):
        p_val = p
        q_val = q
        p_and_q = 'T' if p_val == 'T' and q_val == 'T' else 'F'
        p_or_q = 'T' if p_val == 'T' or q_val == 'T' else 'F'
        not_p = 'F' if p_val == 'T' else 'T'
        row_output = f"{p_val} | {q_val} | {p_and_q} | {p_or_q} | {not_p}"
        print(row_output)
if __name__ == '__main__':
    sample_inputs = [
        ('T', 'T'),
        ('T', 'F'),
        ('F', 'T'),
        ('F', 'F')
    ]
    print_truth_table(sample_inputs)