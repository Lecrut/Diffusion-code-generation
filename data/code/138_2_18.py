import itertools

def truth_table(operator):
    inputs = list(itertools.product([False, True], repeat=2))
    results = []
    for a, b in inputs:
        if operator == 'AND':
            result = a and b
        elif operator == 'OR':
            result = a or b
        elif operator == 'NOT':
            result = not a
        elif operator == 'XOR':
            result = a != b
        elif operator == 'NOR':
            result = not (a or b)
        elif operator == 'NAND':
            result = not (a and b)
        results.append((a, b, result))
    return results

if __name__ == '__main__':
    print(truth_table('AND'))
    print(truth_table('OR'))
    print(truth_table('NOT'))
    print(truth_table('XOR'))
    print(truth_table('NOR'))
    print(truth_table('NAND'))