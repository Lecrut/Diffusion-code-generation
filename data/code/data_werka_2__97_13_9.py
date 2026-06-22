OPERATOR_TABLE = {
    'AND': lambda x, y: x and y
}

def generate_truth_table(operands, operator_name):
    results = []
    operator_func = OPERATOR_TABLE[operator_name]
    for val_a in operands:
        for val_b in operands:
            computed_result = operator_func(val_a, val_b)
            results.append((val_a, val_b, computed_result))
    return results

if __name__ == '__main__':
    sample_inputs = [True, False]
    truth_data = generate_truth_table(sample_inputs, 'AND')
    for entry in truth_data:
        print(entry)