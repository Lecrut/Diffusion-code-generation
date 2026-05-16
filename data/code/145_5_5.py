import ast
def safe_evaluate_boolean_structure(expression, context=None):
    if context is None:
        context = {}
    try:
        node = ast.parse(expression, mode='eval')
        def _eval(node, current_context):
            if isinstance(node, ast.Expression):
                return _eval(node.body, current_context)
            elif isinstance(node, ast.Constant):
                return node.value
            elif isinstance(node, ast.Name):
                if node.id in current_context:
                    return current_context[node.id]
                else:
                    raise NameError(f"Variable {node.id} not defined in context")
            elif isinstance(node, ast.BoolOp):
                op = None
                values = []
                for item in node.values:
                    if isinstance(item, ast.BoolOp):
                        pass
                    values.extend(_eval(item, current_context))
                if isinstance(node.op, ast.And):
                    return all(values)
                elif isinstance(node.op, ast.Or):
                    return any(values)
                elif isinstance(node.op, ast.Not):
                    if len(values) == 1:
                        return not values[0]
                    else:
                        raise TypeError("Not operator expects a single operand")
                else:
                    raise TypeError(f"Unsupported boolean operator: {type(node.op)}")
            elif isinstance(node, ast.UnaryOp):
                operand = _eval(node.operand, current_context)
                if isinstance(node.op, ast.Not):
                    return not operand
                elif isinstance(node.op, ast.NotEq):
                    return not operand
                else:
                    raise TypeError(f"Unsupported unary operator: {type(node.op)}")
            else:
                raise TypeError(f"Unsupported AST node type: {type(node)}")
        return _eval(node, context)
    except Exception as e:
        return f"Error during evaluation: {e}"
if __name__ == '__main__':
    expression1 = "(True and False) or (not False)"
    context1 = {"True": True, "False": False}
    result1 = safe_evaluate_boolean_structure(expression1, context1)
    print(f"Expression: {expression1}")
    print(f"Result 1: {result1}")
    expression2 = "not (True and False)"
    context2 = {"True": True, "False": False}
    result2 = safe_evaluate_boolean_structure(expression2, context2)
    print(f"Expression: {expression2}")
    print(f"Result 2: {result2}")
    expression3 = "not (False or False)"
    context3 = {"True": True, "False": False}
    result3 = safe_evaluate_boolean_structure(expression3, context3)
    print(f"Expression: {expression3}")
    print(f"Result 3: {result3}")
    expression4 = "True or (False and True)"
    context4 = {"True": True, "False": False}
    result4 = safe_evaluate_boolean_structure(expression4, context4)
    print(f"Expression: {expression4}")
    print(f"Result 4: {result4}")
    expression5 = "not (True and not False)"
    context5 = {"True": True, "False": False}
    result5 = safe_evaluate_boolean_structure(expression5, context5)
    print(f"Expression: {expression5}")
    print(f"Result 5: {result5}")
    expression6 = "not (True or False)"
    context6 = {"True": True, "False": False}
    result6 = safe_evaluate_boolean_structure(expression6, context6)
    print(f"Expression: {expression6}")
    print(f"Result 6: {result6}")