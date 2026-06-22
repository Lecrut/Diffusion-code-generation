TRUE_VAL = True
FALSE_VAL = False

def evaluate_logic(p, q):
    r = p ^ q
    first_part = p and q
    second_part = (not p) and r
    return first_part or second_part

if __name__ == '__main__':
    cases = [
        (TRUE_VAL, TRUE_VAL),
        (TRUE_VAL, FALSE_VAL),
        (FALSE_VAL, TRUE_VAL),
        (FALSE_VAL, FALSE_VAL)
    ]
    output_map = {}
    for p_val, q_val in cases:
        output_map[(p_val, q_val)] = evaluate_logic(p_val, q_val)
    print(output_map)