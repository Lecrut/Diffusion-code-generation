def print_truth_table(inputs):
    if not inputs:
        return
    headers = ['P', 'Q', 'P AND Q', 'P OR Q', 'P XOR Q', 'NOT P', 'P IMPLIES Q']
    print(f"{headers[0]:<5} {headers[1]:<5} {headers[2]:<10} {headers[3]:<10} {headers[4]:<10} {headers[5]:<10} {headers[6]:<15}")
    print("-" * 60)
    for p, q in inputs:
        p_and_q = p and q
        p_or_q = p or q
        p_xor_q = p != q
        not_p = not p
        p_implies_q = (not p) or q
        print(f"{str(p):<5} {str(q):<5} {str(p_and_q):<10} {str(p_or_q):<10} {str(p_xor_q):<10} {str(not_p):<10} {str(p_implies_q):<15}")

if __name__ == '__main__':
    sample_inputs = [(True, True), (True, False), (False, True), (False, False)]
    print_truth_table(sample_inputs)