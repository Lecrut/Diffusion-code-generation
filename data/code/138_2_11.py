import itertools

def generate_truth_table(operator):
    operators = {
        'AND': lambda a, b: a and b,
        'OR': lambda a, b: a or b,
        'NOT': lambda a: not a,
        'XOR': lambda a, b: a != b,
        'NOR': lambda a, b: not (a or b),
        'NAND': lambda a, b: not (a and b)
    }
    if operator in operators:
        inputs = [False, True]
        if operator == 'NOT':
            return {operator: [(x, operators[operator](x)) for x in inputs]}
        else:
            return {operator: [(x, y, operators[operator](x, y)) for x, y in itertools.product(inputs, repeat=2)]}
    else:
        raise ValueError("Invalid operator")

if __name__ == '__main__':
    print(generate_truth_table('AND'))
    print(generate_truth_table('OR'))
    print(generate_truth_table('NOT'))
    print(generate_truth_table('XOR'))
    print(generate_truth_table('NOR'))
    print(generate_truth_table('NAND'))