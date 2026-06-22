def generate_truth_table(inputs):
    if not inputs:
        return []
    results = []
    for p, q in inputs:
        p_and_q = p and q
        p_or_q = p or q
        p_xor_q = p != q
        not_p = not p
        p_implies_q = (not p) or q
        results.append({
            'P': p,
            'Q': q,
            'P AND Q': p_and_q,
            'P OR Q': p_or_q,
            'P XOR Q': p_xor_q,
            'NOT P': not_p,
            'P IMPLIES Q': p_implies_q
        })
    return results

def format_truth_table(data):
    if not data:
        return ""
    headers = ['P', 'Q', 'P AND Q', 'P OR Q', 'P XOR Q', 'NOT P', 'P IMPLIES Q']
    widths = [5, 5, 9, 9, 9, 7, 13]
    header_line = " ".join(f"{h:<{w}}" for h, w in zip(headers, widths))
    separator = "-" * sum(widths) + " " * (len(headers) - 1)
    lines = [header_line, separator]
    for row in data:
        values = [row[h] for h in headers]
        line = " ".join(f"{str(v):<{w}}" for v, w in zip(values, widths))
        lines.append(line)
    return "\n".join(lines)

if __name__ == '__main__':
    sample_inputs = [(True, True), (True, False), (False, True), (False, False)]
    table_data = generate_truth_table(sample_inputs)
    print(format_truth_table(table_data))