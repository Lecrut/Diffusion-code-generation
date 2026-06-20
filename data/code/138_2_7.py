import itertools

def truth_table(operator):
    operators = {
        'AND': lambda x, y: x and y,
        'OR': lambda x, y: x or y,
        'NOT': lambda x: not x,
        'XOR': lambda x, y: x != y,
        'NOR': lambda x, y: not (x or y),
        'NAND': lambda x, y: not (x and y)
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