def test_nested_logic(test_cases):
    results = {}
    for name, expected, actual in test_cases.items():
        results[name] = {"expected": expected, "actual": actual}
    return results
def evaluate_expression(expression, context):
    if isinstance(expression, bool):
        return expression
    elif isinstance(expression, dict):
        return {k: evaluate_expression(v, context) for k, v in expression.items()}
    elif isinstance(expression, list):
        return [evaluate_expression(item, context) for item in expression]
    elif isinstance(expression, str):
        if expression == "True":
            return True
        elif expression == "False":
            return False
        elif expression.isdigit():
            return int(expression)
        else:
            raise ValueError(f"Unknown string value: {expression}")
    else:
        return expression
def run_test_case(expression, context):
    try:
        actual = evaluate_expression(expression, context)
    except Exception as e:
        actual = f"Error: {e}"
    return actual
if __name__ == '__main__':
    test_data = {
        "simple_and": {
            "expression": "True and False",
            "expected": False,
            "actual": None
        },
        "nested_dict_logic": {
            "expression": {"a": True, "b": False},
            "expected": {"a": False, "b": False},
            "actual": None
        },
        "list_operation": {
            "expression": [True, False, True],
            "expected": [True, False, True],
            "actual": None
        },
        "complex_nesting": {
            "expression": {"level1": [True, False], "level2": {"x": True}},
            "expected": {"level1": [True, False], "level2": {"x": True}},
            "actual": None
        },
        "string_conversion": {
            "expression": "True or 1",
            "expected": True,
            "actual": None
        }
    }
    test_results = {}
    for name, data in test_data.items():
        expression = data["expression"]
        expected = data["expected"]
        actual = run_test_case(expression, {})
        test_results[name] = {
            "expected": expected,
            "actual": actual
        }
    print(test_results)