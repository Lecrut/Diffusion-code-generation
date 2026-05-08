import ast
def safe_eval_boolean(expression, context=None):
    try:
        node = ast.parse(expression, mode='eval')
        if isinstance(node.body, ast.Expression):
            body = node.body
            if isinstance(body.value, ast.BoolOp):
                result = []
                for item in body.values:
                    item_value = safe_eval_boolean(ast.Expression(item), context)
                    result.append(item_value)
                if isinstance(body.op, ast.And):
                    return all(result)
                elif isinstance(body.op, ast.Or):
                    return any(result)
                elif isinstance(body.op, ast.Not):
                    if len(result) == 1:
                        return not result[0]
                    else:
                        raise ValueError("Invalid structure for 'not' operation on multiple values")
                else:
                    raise ValueError(f"Unsupported boolean operator: {type(body.op)}")
            elif isinstance(body.value, ast.Bool):
                return body.value.value
        else:
            raise ValueError("Expression must be a boolean expression")
    except Exception as e:
        raise ValueError(f"Error evaluating expression: {e}")
def evaluate_nested_boolean(nested_bools):
    if not isinstance(nested_bools, list):
        raise TypeError("Input must be a list of boolean structures")
    def recursive_eval(data):
        if isinstance(data, bool):
            return data
        if isinstance(data, dict):
            return {k: recursive_eval(v) for k, v in data.items()}
        if isinstance(data, list):
            return [recursive_eval(item) for item in data]
        try:
            return data
        except Exception:
            return data
    return recursive_eval(nested_bools)
if __name__ == '__main__':
    structure1 = [True, False, (True and False)]
    structure2 = [True or False, not (True and False)]
    structure3 = [True, True, True]
    structure4 = [False, False, False]
    structure5 = [True, (False or True)]
    print(f"Structure 1: {structure1}")
    print(f"Evaluation 1: {evaluate_nested_boolean(structure1)}")
    print(f"\nStructure 2: {structure2}")
    print(f"Evaluation 2: {evaluate_nested_boolean(structure2)}")
    print(f"\nStructure 3: {structure3}")
    print(f"Evaluation 3: {evaluate_nested_boolean(structure3)}")
    print(f"\nStructure 4: {structure4}")
    print(f"Evaluation 4: {evaluate_nested_boolean(structure4)}")
    print(f"\nStructure 5: {structure5}")
    print(f"Evaluation 5: {evaluate_nested_boolean(structure5)}")
    try:
        safe_test_expr = "True and (False or True)"
        result = safe_eval_boolean(safe_test_expr)
        print(f"\nSafe Eval Test ('{safe_test_expr}'): {result}")
    except ValueError as e:
        print(f"\nSafe Eval Error: {e}")