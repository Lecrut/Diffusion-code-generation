def print_truth_table(inputs):
    if not inputs:
        return
    headers = ['P', 'Q', 'P AND Q', 'P OR Q', 'P XOR Q', 'NOT P', 'P IMPLIES Q']
    print(f"{'P':<5} {'Q':<5} {'AND':<5} {'OR':<5} {'XOR':<5} {'NOT P':<7} {'IMPLIES':<10}")
    print("-" * 45)
    for p, q in inputs:
        and_res = p and q
        or_res = p or q
        xor_res = p ^ q
        not_p = not p
        implies_res = (not p) or q
        print(f"{str(p):<5} {str(q):<5} {str(and_res):<5} {str(or_res):<5} {str(xor_res):<5} {str(not_p):<7} {str(implies_res):<10}")

if __name__ == '__main__':
    sample_inputs = [
        (True, True),
        (True, False),
        (False, True),
        (False, False)
    ]
    print_truth_table(sample_inputs)