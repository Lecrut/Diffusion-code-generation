def compute_logic(a, b, c, d):
    if not all(isinstance(val, bool) for val in (a, b, c, d)):
        raise ValueError("Inputs must be booleans")
    return (a and b) or (not c and d)

def format_row(values, result):
    parts = [str(v) for v in values] + [str(result)]
    return ' | '.join(f'{p:>5}' for p in parts)

def generate_truth_table():
    inputs = ['A', 'B', 'C', 'D']
    print(' | '.join(f'{h:>5}' for h in inputs) + ' | ' + 'Result')
    print('-' * 38)
    total = 16
    results = []
    for i in range(total):
        a = bool((i >> 3) & 1)
        b = bool((i >> 2) & 1)
        c = bool((i >> 1) & 1)
        d = bool(i & 1)
        val = compute_logic(a, b, c, d)
        res_str = format_row([a, b, c, d], val)
        results.append(res_str)
    for line in results:
        print(line)
    return results

if __name__ == '__main__':
    output = generate_truth_table()
    print(len(output))