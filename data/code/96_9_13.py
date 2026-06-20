def validate_input(nested):
    if not isinstance(nested, (list, tuple)):
        return False
    operator = nested[0]
    if operator not in ('and', 'or', 'not'):
        return False
    operands = nested[1:]
    if operator == 'not':
        return len(operands) == 1 and validate_input(operands[0])
    for operand in operands:
        if not validate_input(operand):
            return False
    return True

def evaluate_nested_logic(nested):
    if not validate_input(nested):
        raise ValueError('Invalid input')
    operator = nested[0]
    operands = nested[1:]
    if operator == 'and':
        return all((evaluate_nested_logic(op) for op in operands))
    elif operator == 'or':
        return any((evaluate_nested_logic(op) for op in operands))
    else:
        return not evaluate_nested_logic(operands[0])
if __name__ == '__main__':
    sample_input = ['and', [True, False], ['or', True, False]]
    print(evaluate_nested_logic(sample_input))