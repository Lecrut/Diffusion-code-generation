NAND = lambda a, b: not (a and b)
OPERATORS = {
    'nand': NAND,
}

def generate_truth_table(operator):
    results = []
    for a in [True, False]:
        for b in [True, False]:
            result = OPERATORS[operator](a, b)
            results.append((a, b, result))
    return results

if __name__ == '__main__':
    operator_nand = 'nand'
    truth_table_nand = generate_truth_table(operator_nand)
    print(f"Truth Table for {operator_nand}:")
    for row in truth_table_nand:
        print(row)