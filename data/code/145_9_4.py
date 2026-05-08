def evaluate_nested_boolean(expression, values):
    def parse_and_evaluate(expr, vals):
        if isinstance(expr, bool):
            return expr
        elif isinstance(expr, str):
            if expr in ('True', 'true', '1'):
                return True
            elif expr in ('False', 'false', '0'):
                return False
            else:
                raise ValueError(f"Unknown boolean string: {expr}")
        elif isinstance(expr, dict):
            result = {}
            for key, value in expr.items():
                result[key] = parse_and_evaluate(value, vals)
            return result
        elif isinstance(expr, list):
            return [parse_and_evaluate(item, vals) for item in expr]
        elif isinstance(expr, tuple):
            return tuple(parse_and_evaluate(item, vals) for item in expr)
        elif isinstance(expr, bool):
            return expr
        else:
            if isinstance(expr, int):
                return bool(expr)
            elif isinstance(expr, float):
                return bool(expr)
            else:
                raise TypeError(f"Unsupported type encountered: {type(expr)}")
        return expr
    return parse_and_evaluate(expression, values)
if __name__ == '__main__':
    test_cases = [
        (
            "((A and B) or C) and (D or (E and not F))",
            {"A": True, "B": False, "C": True, "D": False, "E": True, "F": False}
        ),
        (
            "not (A or B) and (C and not D)",
            {"A": True, "B": True, "C": False, "D": True}
        ),
        (
            "A or (B and (C or D))",
            {"A": False, "B": True, "C": False, "D": False}
        ),
        (
            "True and (False or (True and False))",
            {"True": True, "False": False, "True": True, "False": False}
        ),
        (
            "1 and not 0",
            {"1": 1, "0": 0}
        ),
        (
            "((10 > 5) and 2 < 3)",
            {"10 > 5": True, "2 < 3": True}
        ),
        (
            "((A and B) or C)",
            {"A": True, "B": True, "C": False}
        )
    ]
    for expression, values in test_cases:
        try:
            result = evaluate_nested_boolean(expression, values)
            print(f"Expression: {expression}")
            print(f"Values: {values}")
            print(f"Result: {result}")
            print("-" * 20)
        except Exception as e:
            print(f"Error evaluating expression: {e}")
            print("-" * 20)