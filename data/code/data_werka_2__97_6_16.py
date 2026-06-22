TRUE_VAL = True
FALSE_VAL = False
SEPARATOR_CHAR = '-'
HEADER_WIDTHS = {'P': 4, 'Q': 4, 'AND': 6, 'OR': 4, 'XOR': 6, 'NOT': 5, 'IMP': 11}
COLUMNS = ['P', 'Q', 'P AND Q', 'P OR Q', 'P XOR Q', 'NOT P', 'P IMPLIES Q']
LOGIC_COLS = ['AND', 'OR', 'XOR', 'NOT', 'IMP']

def compute_row(p_val, q_val):
    results = {}
    results['P'] = p_val
    results['Q'] = q_val
    results['AND'] = p_val and q_val
    results['OR'] = p_val or q_val
    results['XOR'] = p_val ^ q_val
    results['NOT'] = not p_val
    results['IMP'] = (not p_val) or q_val
    return results

def format_value(val, width):
    s = str(val).upper()
    return s.ljust(width)

def print_header():
    fmt = f"{format_value('P', HEADER_WIDTHS['P'])} {format_value('Q', HEADER_WIDTHS['Q'])} {format_value('P AND Q', HEADER_WIDTHS['AND'])} {format_value('P OR Q', HEADER_WIDTHS['OR'])} {format_value('P XOR Q', HEADER_WIDTHS['XOR'])} {format_value('NOT P', HEADER_WIDTHS['NOT'])} {format_value('P IMPLIES Q', HEADER_WIDTHS['IMP'])}"
    print(fmt)

def print_separator():
    total_width = sum(HEADER_WIDTHS.values()) + (len(HEADER_WIDTHS) - 1)
    print(SEPARATOR_CHAR * total_width)

def print_row(row_data):
    vals = [
        row_data['P'],
        row_data['Q'],
        row_data['AND'],
        row_data['OR'],
        row_data['XOR'],
        row_data['NOT'],
        row_data['IMP']
    ]
    widths = [
        HEADER_WIDTHS['P'],
        HEADER_WIDTHS['Q'],
        HEADER_WIDTHS['AND'],
        HEADER_WIDTHS['OR'],
        HEADER_WIDTHS['XOR'],
        HEADER_WIDTHS['NOT'],
        HEADER_WIDTHS['IMP']
    ]
    parts = [format_value(v, w) for v, w in zip(vals, widths)]
    print(' '.join(parts))

def print_truth_table(inputs):
    if not inputs:
        return
    print_header()
    print_separator()
    for p, q in inputs:
        row = compute_row(p, q)
        print_row(row)

if __name__ == '__main__':
    sample_inputs = [
        (TRUE_VAL, TRUE_VAL),
        (TRUE_VAL, FALSE_VAL),
        (FALSE_VAL, TRUE_VAL),
        (FALSE_VAL, FALSE_VAL)
    ]
    print_truth_table(sample_inputs)