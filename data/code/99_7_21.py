def evaluate_boolean_expression(expression: str) -> bool:
    try:
        result = eval(expression, {"__builtins__": {}}, {})
        if not isinstance(result, bool):
            raise ValueError("Expression did not evaluate to a boolean")
        return result
    except SyntaxError:
        raise ValueError("Invalid syntax in boolean expression")
    except NameError:
        raise ValueError("Undefined variable in expression")
    except ZeroDivisionError:
        raise ValueError("Division by zero in expression")
    except Exception as e:
        raise ValueError(f"Error evaluating expression: {e}")

if __name__ == '__main__':
    print(evaluate_boolean_expression("True and False"))
    print(evaluate_boolean_expression("10 > 5 or 1 == 2"))
    print(evaluate_boolean_expression("not (5 < 3)"))
    print(evaluate_boolean_expression("2 + 2 == 4 and 10 / 2 == 5"))