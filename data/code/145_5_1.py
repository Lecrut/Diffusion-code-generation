import ast
def safe_eval_boolean(expression, context=None):
    if context is None:
        context = {}
    try:
        node = ast.parse(expression, mode='eval').body
        if isinstance(node, ast.Expression):
            body = node.body
        else:
            body = node
        result = eval(compile(ast.dump(body), filename='<string>', mode='eval'), '<string>', context)
        return bool(result)
    except Exception:
        return False
def evaluate_nested_boolean(nested_structure):
    def recursive_eval(data):
        if isinstance(data, bool):
            return data
        elif isinstance(data, dict):
            return {k: recursive_eval(v) for k, v in data.items()}
        elif isinstance(data, list):
            return [recursive_eval(item) for item in data]
        else:
            return data
    return recursive_eval(nested_structure)
if __name__ == '__main__':
    test_structure = {
        "level1": True,
        "level2": {
            "level3a": False,
            "level3b": {
                "level4a": 1,
                "level4b": {"level5a": True, "level5b": False}
            }
        },
        "level1_false": False,
        "level1_list": [True, False, {"nested_bool": True}]
    }
    evaluated_structure = evaluate_nested_boolean(test_structure)
    print(evaluated_structure)