import ast
def safe_evaluate(expression, context=None):
    if context is None:
        context = {}
    try:
        node = ast.parse(expression, mode='eval')
        def _eval(node, current_context):
            if isinstance(node, ast.Expression):
                return _eval(node.body, current_context)
            elif isinstance(node, ast.Constant):
                if isinstance(node.value, bool):
                    return node.value
                elif isinstance(node.value, int):
                    return bool(node.value)
                elif isinstance(node.value, str):
                    return bool(node.value)
                elif isinstance(node.value, list):
                    return all(_eval(item, current_context) for item in node.elts)
                elif isinstance(node.value, dict):
                    return all(_eval(k, current_context) for k in node.keys)
                else:
                    return bool(node.value)
            elif isinstance(node, ast.Name):
                if node.id in current_context:
                    return current_context[node.id]
                else:
                    raise NameError(f"Name '{node.id}' not defined in context")
            elif isinstance(node, ast.BoolOp):
                if isinstance(node.op, (ast.And, ast.Or)):
                    if isinstance(node.op, ast.And):
                        return all(_eval(child, current_context) for child in node.values)
                    elif isinstance(node.op, ast.Or):
                        return any(_eval(child, current_context) for child in node.values)
            elif isinstance(node, ast.UnaryOp):
                operand = _eval(node.operand, current_context)
                if isinstance(node.op, ast.Not):
                    return not operand
                elif isinstance(node.op, ast.NotEq):
                    return operand != node.operand
                elif isinstance(node.op, ast.NotGt):
                    return operand < node.operand
                elif isinstance(node.op, ast.NotLt):
                    return operand > node.operand
                elif isinstance(node.op, ast.NotEq):
                    return operand != node.operand
                else:
                    return operand
            else:
                raise TypeError(f"Unsupported AST node type: {type(node)}")
        return _eval(node, context)
    except Exception as e:
        raise ValueError(f"Error during safe evaluation: {e}")
if __name__ == '__main__':
    nested_bool_structure = {
        "a": True,
        "b": False,
        "c": None,
        "d": [True, False],
        "e": {"x": True, "y": False},
        "f": [True, True]
    }
    def get_value(key):
        return nested_bool_structure.get(key)
    def evaluate_nested(structure):
        def recursive_eval(node):
            if isinstance(node, dict):
                return {k: recursive_eval(v) for k, v in node.items()}
            elif isinstance(node, list):
                return [recursive_eval(item) for item in node]
            elif isinstance(node, bool):
                return node
            else:
                return node
        return recursive_eval(structure)
    result = evaluate_nested(nested_bool_structure)
    print(f"Original structure: {nested_bool_structure}")
    print(f"Evaluated structure: {result}")
    print("\nTesting specific truth values directly:")
    print(f"a is True: {nested_bool_structure['a']}")
    print(f"b is False: {nested_bool_structure['b']}")
    print(f"d[0] is True: {nested_bool_structure['d'][0]}")
    print(f"e['x'] is True: {nested_bool_structure['e']['x']}")
    print(f"e['y'] is False: {nested_bool_structure['e']['y']}")
    print(f"f[0] is True: {nested_bool_structure['f'][0]}")
    print(f"d is all True: {all(nested_bool_structure['d'])}")
    print(f"e is all True: {all(nested_bool_structure['e'].values())}")
    print(f"f is all True: {all(nested_bool_structure['f'])}")