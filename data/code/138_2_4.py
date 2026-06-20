import itertools

def truth_table(operator):
    operators = {
        'AND': lambda a, b: a and b,
        'OR': lambda a, b: a or b,
        'NOT': lambda a: not a,
        'XOR': lambda a, b: a != b,
        'NOR': lambda a, b: not (a or b),
        'NAND': lambda a, b: not (a and b)
    }
    if operator in operators:
        return {inputs: operators[operator](*inputs) for inputs in itertools.product([False, True], repeat=2)}
    else:
        raise ValueError("Invalid operator")

if __name__ == '__main__':
    print(truth_table('AND'))
    print(truth_table('OR'))
    print(truth_table('NOT'))
    print(truth_table('XOR'))
    print(truth_table('NOR'))
    print(truth_table('NAND'))