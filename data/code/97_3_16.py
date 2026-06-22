def generate_implication_table():
    TRUE_VAL = True
    FALSE_VAL = False
    VARIABLE_DOMAIN = [FALSE_VAL, TRUE_VAL]
    HEADER = f"{'P':<5} {'Q':<5} {'P -> Q':<8}"
    ROWS = []
    for p_val in VARIABLE_DOMAIN:
        for q_val in VARIABLE_DOMAIN:
            result = (not p_val) or q_val
            ROWS.append((p_val, q_val, result))
    return HEADER, ROWS

def print_truth_table(HEADER, ROWS):
    print(HEADER)
    for p_val, q_val, impl_val in ROWS:
        print(f"{str(p_val):<5} {str(q_val):<5} {str(impl_val):<8}")

if __name__ == '__main__':
    HEADER, ROWS = generate_implication_table()
    print_truth_table(HEADER, ROWS)