def safe_evaluate(expression, context=None):
    if context is None:
        context = {}
    try:
        result = eval(expression, {"__builtins__": None}, context)
        if not isinstance(result, bool):
            raise TypeError("Expression did not evaluate to a boolean.")
        return result
    except Exception:
        return False
if __name__ == '__main__':
    nested_bool_structure = {
        "level1": True,
        "level2": {
            "level3_a": False,
            "level3_b": True,
            "level3_c": {
                "level4_x": 1,
                "level4_y": False
            }
        },
        "level1_false": False
    }
    def recursive_check(data):
        if isinstance(data, bool):
            return data
        elif isinstance(data, dict):
            all_true = True
            for value in data.values():
                if not recursive_check(value):
                    all_true = False
            return all_true
        elif isinstance(data, list):
            all_true = True
            for item in data:
                if not recursive_check(item):
                    all_true = False
            return all_true
        else:
            return False
    result = recursive_check(nested_bool_structure)
    print(result)