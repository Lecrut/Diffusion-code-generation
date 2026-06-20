def boolean_operation(a, b, op):
    if op == 'AND':
        return a and b
    elif op == 'OR':
        return a or b
    elif op == 'NOT':
        return not b
    elif op == 'XOR':
        return a != b
    elif op == 'NAND':
        return not (a and b)
    elif op == 'NOR':
        return not (a or b)
    elif op == 'IMPLIES':
        return not a or b
    else:
        raise ValueError("Invalid operation")

def generate_truth_table():
    results = {}
    pairs = [(True, True), (True, False), (False, True), (False, False)]
    ops = ['AND', 'OR', 'NOT', 'XOR', 'NAND', 'NOR', 'IMPLIES']
    
    for a, b in pairs:
        for op in ops:
            result = boolean_operation(a, b, op)
            key = f"{a}_{b}_{op}"
            results[key] = result
    
    return results

if __name__ == '__main__':
    truth_table = generate_truth_table()
    print(truth_table)