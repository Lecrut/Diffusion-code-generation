def evaluate_nested_logic(nested):
    if isinstance(nested, (list, tuple)):
        operator = nested[0]
        operands = nested[1:]
        if operator == 'and':
            return all(evaluate_nested_logic(op) for op in operands)
        elif operator == 'or':
            return any(evaluate_nested_logic(op) for op in operands)
        elif operator == 'not':
            if len(operands) != 1:
                raise ValueError("Not operator requires exactly one operand")
            return not evaluate_nested_logic(operands[0])
        else:
            raise ValueError(f"Invalid operator: {operator}")
    else:
        try:
            return bool(nested)
        except Exception as e:
            raise ValueError(f"Invalid input type: {type(nested)}") from e

if __name__ == '__main__':
    print(evaluate_nested_logic(('and', True, False)))
    print(evaluate_nested_logic(('or', True, False)))
    print(evaluate_nested_logic(('not', False)))
    try:
        print(evaluate_nested_logic(('invalid_operator', True)))
    except ValueError as e:
        print(f"Caught exception: {e}")