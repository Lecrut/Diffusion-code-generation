def evaluate_boolean_expression(expression, inputs):
    def evaluate_term(term, values):
        if term == 'T':
            return True
        elif term == 'F':
            return False
        else:
            return values.get(term, False)
    tokens = expression.upper().split()
    if len(tokens) != 3:
        raise ValueError("Invalid expression format. Expected 'P OP Q'.")
    if tokens[0] not in ['P', 'Q']:
        raise ValueError("Only variables P and Q are supported.")
    var1 = tokens[0]
    op = tokens[1]
    var2 = tokens[2]
    if var1 not in inputs or var2 not in inputs:
        raise ValueError("Input variables must be present in the inputs dictionary.")
    val1 = inputs[var1]
    val2 = inputs[var2]
    if op == 'AND':
        return val1 and val2
    elif op == 'OR':
        return val1 or val2
    elif op == 'XOR':
        return val1 ^ val2
    elif op == 'NOT':
        raise ValueError("Only binary operators (AND, OR, XOR) are supported in this simplified structure.")
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
        ('P OR Q', {'P': False, 'Q': True}),
        ('P OR Q', {'P': False, 'Q': False}),
        ('P XOR Q', {'P': True, 'Q': True}),
    ]
    for expression, inputs in test_cases:
        try:
            result = evaluate_boolean_expression(expression, inputs)
            print(f"Expression: {expression}, Inputs: {inputs}")
            print(f"Result: {result}\n")
        except ValueError as e:
            print(f"Error evaluating '{expression}': {e}\n")
        except Exception as e:
            print(f"An unexpected error occurred for '{expression}': {e}\n")