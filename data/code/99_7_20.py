def evaluate_boolean_expression(expression: str) -> bool:
    try:
        result = eval(expression)
        if not isinstance(result, bool):
            raise ValueError("Expression did not evaluate to a boolean")
        return result
    except Exception as e:
        raise ValueError(f"Invalid boolean expression: {e}")

if __name__ == '__main__':
    print(evaluate_boolean_expression("True and False"))
    print(evaluate_boolean_expression("10 > 5 or 1 < 2"))
    print(evaluate_boolean_expression("not True"))
    print(evaluate_boolean_expression("(2 + 2) == 4 and 5 > 3"))