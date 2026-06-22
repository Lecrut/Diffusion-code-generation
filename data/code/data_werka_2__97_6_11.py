def generate_truth_table(pairs):
    if not pairs:
        return []
    results = []
    for p, q in pairs:
        conjunction = p and q
        disjunction = p or q
        exclusive_or = p ^ q
        negation = not p
        implication = not p or q
        biconditional = p == q
        row = {'P': p, 'Q': q, 'AND': conjunction, 'OR': disjunction, 'XOR': exclusive_or, 'NOT_P': negation, 'IMPLIES': implication, 'IFF': biconditional}
        results.append(row)
    return results

def display_table(data):
    if not data:
        return
    col_widths = [5, 5, 7, 7, 7, 8, 11, 7]
    headers = ['P', 'Q', 'AND', 'OR', 'XOR', 'NOT P', 'IMPLIES', 'IFF']
    header_line = ' '.join((f'{h:<{w}}' for h, w in zip(headers, col_widths)))
    print(header_line)
    print('-' * sum(col_widths) + len(col_widths) - 1 * ' ')
    for row in data:
        values = [row['P'], row['Q'], row['AND'], row['OR'], row['XOR'], row['NOT_P'], row['IMPLIES'], row['IFF']]
        val_strs = [str(v) for v in values]
        print(' '.join((f'{v:<{w}}' for v, w in zip(val_strs, col_widths))))
if __name__ == '__main__':
    test_cases = [(True, True), (False, True), (True, False), (False, False)]
    table_data = generate_truth_table(test_cases)
    display_table(table_data)