def evaluate_boolean_expression(expression, context):
    if not isinstance(expression, str):
        return expression
    tokens = expression.split()
    if not tokens:
        raise ValueError("Empty expression")
    result_stack = []
    operator_stack = []
    values_stack = []
    def apply_op(op, b, a):
        if op == 'AND':
            return a and b
        elif op == 'OR':
            return a or b
        elif op == 'NOT':
            return not a
        elif op == 'NOT_GROUP':
            return not b
        else:
            raise ValueError(f"Unknown operator: {op}")
    for token in tokens:
        if token.lower() == 'and':
            operator_stack.append('AND')
            pass
        elif token.lower() == 'or':
            operator_stack.append('OR')
            pass
        elif token.lower() == 'not':
            operator_stack.append('NOT')
            pass
        elif token in ('True', 'False'):
            values_stack.append(token == 'True')
        else:
            try:
                values_stack.append(eval(token))
            except NameError:
                raise ValueError(f"Invalid token: {token}")
    def parse_expression(tokens_list):
        if not tokens_list:
            return False
        if tokens_list[0] == 'NOT':
            result = parse_expression(tokens_list[1:])
            return not result
        operands = []
        current_op = None
        i = 0
        while i < len(tokens_list):
            token = tokens_list[i]
            if token in ('True', 'False'):
                operands.append(token == 'True')
                i += 1
            elif token == 'NOT':
                next_operand = parse_expression(tokens_list[i+1:])
                operands.append(not next_operand)
                i += len(tokens_list[i+1:]) - 1                                       
            elif token in ('AND', 'OR'):
                pass
            else:
                try:
                    operands.append(eval(token))
                except:
                    raise ValueError(f"Could not evaluate token: {token}")
                i += 1
        return evaluate_string_recursively(expression, context)
    def evaluate_string_recursively(expr, ctx):
        try:
            return eval(expr, {"__builtins__": None}, ctx)
        except Exception as e:
            raise ValueError(f"Evaluation error for '{expr}': {e}")
    return evaluate_string_recursively(expression, context)
if __name__ == '__main__':
    test_cases = [
        ("True and False", {"True": True, "False": False}),
        ("(True or False) and True", {"True": True, "False": False}),
        ("not False", {"True": True, "False": False}),
        ("not (True and False)", {"True": True, "False": False}),
        ("True or (False and True)", {"True": True, "False": False}),
        ("not (True or False)", {"True": True, "False": False}),
        ("True and (False or True)", {"True": True, "False": False}),
        ("not True and False", {"True": True, "False": False}),
    ]
    for expr, ctx in test_cases:
        try:
            result = evaluate_boolean_expression(expr, ctx)
            print(f"Expression: '{expr}' -> Result: {result}")
        except ValueError as e:
            print(f"Error processing '{expr}': {e}")
        except Exception as e:
            print(f"Unexpected error processing '{expr}': {e}")