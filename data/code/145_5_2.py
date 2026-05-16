def safe_evaluate(expression, context=None):
    if context is None:
        context = {}
    local_scope = context.copy()
    try:
        result = eval(expression, {"__builtins__": None}, local_scope)
        return result
    except Exception:
        return False
if __name__ == '__main__':
    nested_bools = {
        "level1": True,
        "level2": {
            "level3_a": False,
            "level3_b": True,
            "level4": {
                "level5_x": True,
                "level5_y": False
            }
        },
        "level1_false": False
    }
    def recursive_check(data, path=None):
        if path is None:
            path = []
        if isinstance(data, bool):
            return data
        if isinstance(data, dict):
            results = {}
            for key, value in data.items():
                new_path = path + [key]
                results[key] = recursive_check(value, new_path)
            return results
        if isinstance(data, list):
            results = []
            for i, item in enumerate(data):
                results.append(recursive_check(item, path + [str(i)]))
            return results
        return data
    all_results = recursive_check(nested_bools)
    print(all_results)