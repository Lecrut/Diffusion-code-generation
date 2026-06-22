def generate_truth_table(inputs):
    if not inputs:
        return []
    headers = ["P", "Q", "AND", "OR", "XOR", "NOT P", "IMPLIES"]
    results = []
    for p, q in inputs:
        and_val = p and q
        or_val = p or q
        xor_val = p != q
        not_p = not p
        implies_val = (not p) or q
        row = {
            "P": p,
            "Q": q,
            "AND": and_val,
            "OR": or_val,
            "XOR": xor_val,
            "NOT P": not_p,
            "IMPLIES": implies_val
        }
        results.append(row)
    return results

def print_table(table_data):
    if not table_data:
        return
    headers = ["P", "Q", "AND", "OR", "XOR", "NOT P", "IMPLIES"]
    widths = {
        "P": 5,
        "Q": 5,
        "AND": 5,
        "OR": 5,
        "XOR": 5,
        "NOT P": 7,
        "IMPLIES": 9
    }
    header_line = "  ".join(f"{h:<{widths[h]}}" for h in headers)
    print(header_line)
    print("-" * len(header_line))
    for row in table_data:
        line = "  ".join(f"{str(row[h]):<{widths[h]}}" for h in headers)
        print(line)

if __name__ == '__main__':
    sample_inputs = [(True, True), (True, False), (False, True), (False, False)]
    truth_table = generate_truth_table(sample_inputs)
    print_table(truth_table)