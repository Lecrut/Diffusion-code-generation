def print_truth_table():
    truth_values = {True: 'T', False: 'F'}
    operators = {'and': '&', 'or': '|', 'not': '!'}
    
    def evaluate_expression(p, q, op):
        if op == 'and':
            return p and q
        elif op == 'or':
            return p or q
        elif op == 'not':
            return not p
    
    print("P | Q | P AND Q | P OR Q | NOT P | NOT Q")
    print("---|---|---------|--------|-------|-------")
    for p in [True, False]:
        for q in [True, False]:
            p_val = truth_values[p]
            q_val = truth_values[q]
            and_result = evaluate_expression(p, q, 'and')
            or_result = evaluate_expression(p, q, 'or')
            not_p = evaluate_expression(p, None, 'not')
            not_q = evaluate_expression(q, None, 'not')
            print(f"{p_val} | {q_val} | {truth_values[and_result]} | {truth_values[or_result]} | {truth_values[not_p]} | {truth_values[not_q]}")

if __name__ == '__main__':
    print_truth_table()