def evaluate_boolean_expression(expression, inputs):
    def parse_and_evaluate(expr, val_map):
        if expr == 'TRUE':
            return True
        elif expr == 'FALSE':
            return False
        else:
            parts = expr.split()
            if len(parts) == 3:
                op = parts[1]
                left_val = val_map[parts[0]]
                right_val = val_map[parts[2]]
                if op == 'AND':
                    return left_val and right_val
                elif op == 'OR':
                    return left_val or right_val
                elif op == 'NOT':
                    return not left_val
                elif op == 'XOR':
                    return left_val ^ right_val
            return None
    result = parse_and_evaluate(expression, inputs)
    return result
if __name__ == '__main__':
    expression1 = 'P AND Q'
    inputs1 = {'P': True, 'Q': False}
    result1 = evaluate_boolean_expression(expression1, inputs1)
    print(f"Expression: {expression1}, Inputs: {inputs1}")
    print(f"Result: {result1}")
    expression2 = '(P OR Q) AND NOT R'
    inputs2 = {'P': True, 'Q': False, 'R': True}
    result2 = evaluate_boolean_expression(expression2, inputs2)
    print(f"Expression: {expression2}, Inputs: {inputs2}")
    print(f"Result: {result2}")
    expression3 = 'P XOR Q'
    inputs3 = {'P': True, 'Q': True}
    result3 = evaluate_boolean_expression(expression3, inputs3)
    print(f"Expression: {expression3}, Inputs: {inputs3}")
    print(f"Result: {result3}")
    expression4 = 'NOT P'
    inputs4 = {'P': False}
    result4 = evaluate_boolean_expression(expression4, inputs4)
    print(f"Expression: {expression4}, Inputs: {inputs4}")
    print(f"Result: {result4}")