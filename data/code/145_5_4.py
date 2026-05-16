def safe_evaluate(expression, context=None):
    if context is None:
        context = {}
    local_scope = context.copy()
    try:
        result = eval(expression, {"__builtins__": {}}, local_scope)
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
                "level5_x": 1,
                "level5_y": "hello"
            }
        },
        "level1_false": False
    }
    def check_truth(data):
        if isinstance(data, bool):
            return data
        elif isinstance(data, dict):
            return all(check_truth(v) for v in data.values())
        elif isinstance(data, list):
            return all(check_truth(item) for item in data)
        else:
            return False
    print(f"Level1 is True: {check_truth(nested_bools['level1'])}")
    print(f"Level1_false is True: {check_truth(nested_bools['level1_false'])}")
    print(f"Level2 is all True: {check_truth(nested_bools['level2'])}")
    print(f"Level3_a is True: {check_truth(nested_bools['level2']['level3_a'])}")
    print(f"Level3_b is True: {check_truth(nested_bools['level2']['level3_b'])}")
    print(f"Level4 is all True: {check_truth(nested_bools['level2']['level4'])}")
    print(f"Level5_x is True: {check_truth(nested_bools['level2']['level4']['level5_x'])}")
    print(f"Level5_y is True: {check_truth(nested_bools['level2']['level4']['level5_y'])}")