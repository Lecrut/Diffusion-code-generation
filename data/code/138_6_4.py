def evaluate_boolean_expression(expression, inputs):
    def parse_and_evaluate(expr, val_map):
        if expr == 'TRUE':
            return True
        elif expr == 'FALSE':
            return False
        else:
            if expr in val_map:
                return val_map[expr]
            else:
                raise ValueError(f"Unknown boolean value: {expr}")
    tokens = expression.upper().split()
    if len(tokens) != 3:
        raise ValueError("Invalid expression format. Expected format: P OP Q")
    if tokens[0] not in ['P', 'Q']:
        raise ValueError("Only variables P and Q are supported in this implementation.")
    var1 = tokens[0]
    op = tokens[1]
    var2 = tokens[2]
    if var1 not in inputs or var2 not in inputs:
        raise ValueError("Inputs must contain values for P and Q.")
    val1 = inputs[var1]
    val2 = inputs[var2]
    if op == 'AND':
        return val1 and val2
    elif op == 'OR':
        return val1 or val2
    elif op == 'XOR':
        return val1 ^ val2
    elif op == 'NOT':
        if var2 == 'P':
            return not val1
        elif var2 == 'Q':
            return not val2
        else:
            raise ValueError("NOT operator only supports NOT P or NOT Q.")
    else:
        raise ValueError(f"Unsupported operator: {op}")
if __name__ == '__main__':
    test_cases = [
        ('P AND Q', {'P': True, 'Q': True}),
        ('P AND Q', {'P': True, 'Q': False}),
        ('P AND Q', {'P': False, 'Q': True}),
        ('P AND Q', {'P': False, 'Q': False}),
        ('P OR Q', {'P': True, 'Q': True}),
        ('P OR Q', {'P': True, 'Q': False}),
        ('P OR Q', {'P': False, 'Q': False}),
        ('P XOR Q', {'P': True, 'Q': True}),
        ('P XOR Q', {'P': True, 'Q': False}),
        ('P XOR Q', {'P': False, 'Q': True}),
        ('P XOR Q', {'P': False, 'Q': False}),
        ('NOT P', {'P': True}),
        ('NOT P', {'P': False}),
        ('NOT Q', {'Q': True}),
        ('NOT Q', {'Q': False}),
    ]
    for expression, inputs in test_cases:
        try:
            result = evaluate_boolean_expression(expression, inputs)
            print(f"Expression: {expression}, Inputs: {inputs}, Result: {result}")
        except ValueError as e:
            print(f"Error evaluating {expression} with inputs {inputs}: {e}")
        print("-" * 20)