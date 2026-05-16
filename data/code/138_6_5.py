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
        raise ValueError("Invalid expression format. Expected 'A OP B'.")
    var1, op, var2 = tokens[0], tokens[1], tokens[2]
    if var1 not in inputs or var2 not in inputs:
        raise ValueError("Input variables not found in the provided inputs.")
    val1 = inputs[var1]
    val2 = inputs[var2]
    if op == 'AND':
        return val1 and val2
    elif op == 'OR':
        return val1 or val2
    elif op == 'XOR':
        return val1 ^ val2
    elif op == 'NOT':
        if var2 not in inputs:
            raise ValueError("NOT operator requires a single operand.")
        return not inputs[var2]
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
        ('P NOT Q', {'P': True, 'Q': True}),
        ('P NOT Q', {'P': True, 'Q': False}),
        ('P NOT Q', {'P': False, 'Q': True}),
        ('P NOT Q', {'P': False, 'Q': False}),
    ]
    for expression, inputs in test_cases:
        try:
            result = evaluate_boolean_expression(expression, inputs)
            print(f"Expression: {expression}, Inputs: {inputs}, Result: {result}")
        except ValueError as e:
            print(f"Error evaluating {expression} with {inputs}: {e}")
        except Exception as e:
            print(f"An unexpected error occurred for {expression}: {e}")
        print("-" * 20)