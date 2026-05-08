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
                raise ValueError("Expression must evaluate to a boolean or boolean operation.")
        else:
            raise ValueError("Expression must be a valid expression.")
    except Exception as e:
        raise ValueError(f"Error evaluating expression: {e}")
def evaluate_nested_boolean(nested_bools):
    if not isinstance(nested_bools, list):
        raise TypeError("Input must be a list of boolean values.")
    if not nested_bools:
        return False
    if len(nested_bools) == 1:
        return nested_bools[0]
    if len(nested_bools) > 1:
        if any(not isinstance(item, bool) for item in nested_bools):
            raise TypeError("All elements in the list must be boolean values.")
        if all(isinstance(item, bool) for item in nested_bools):
            if all(item for item in nested_bools):
                return True
            else:
                return False
        else:
            raise TypeError("List contains non-boolean elements.")
    return False
if __name__ == '__main__':
    sample_structure = [True, False, True, True]
    print(f"Testing simple list evaluation: {evaluate_nested_boolean(sample_structure)}")
    nested_structure_1 = [True, True, False]
    print(f"Testing nested structure 1: {evaluate_nested_boolean(nested_structure_1)}")
    nested_structure_2 = [False, False, False]
    print(f"Testing nested structure 2: {evaluate_nested_boolean(nested_structure_2)}")
    nested_structure_3 = [True, True, True]
    print(f"Testing nested structure 3: {evaluate_nested_boolean(nested_structure_3)}")
    try:
        invalid_structure = [True, "False", True]
        evaluate_nested_boolean(invalid_structure)
    except TypeError as e:
        print(f"Caught expected error for invalid types: {e}")
    try:
        invalid_structure_2 = [True, False, 1]
        evaluate_nested_boolean(invalid_structure_2)
    except TypeError as e:
        print(f"Caught expected error for mixed types: {e}")