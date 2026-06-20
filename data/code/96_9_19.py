def evaluate_nested_logic(nested):
    if not isinstance(nested, (list, tuple)) or len(nested) < 2:
        raise ValueError("Invalid nested structure")
    
    operator = nested[0]
    operands = nested[1:]
    
    if operator == 'and':
        return all(evaluate_nested_logic(op) for op in operands)
    elif operator == 'or':
        return any(evaluate_nested_logic(op) for op in operands)
    elif operator == 'not':
        if len(operands) != 1:
            raise ValueError("Not operation requires exactly one operand")
        return not evaluate_nested_logic(operands[0])
    else:
        raise ValueError(f"Invalid operator: {operator}")

if __name__ == '__main__':
    sample = ['and', [True, ['or', False, True], ['not', False]]]
    print(evaluate_nested_logic(sample))