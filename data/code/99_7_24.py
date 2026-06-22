def evaluate_boolean_expression(expression: str) -> bool:
    if not isinstance(expression, str):
        raise ValueError("Input must be a string")
    sanitized = expression.strip()
    if not sanitized:
        raise ValueError("Empty expression provided")
    try:
        result = eval(sanitized, {"__builtins__": {}}, {})
        if not isinstance(result, bool):
            raise ValueError("Expression did not evaluate to a boolean")
        return result
    except SyntaxError:
        raise ValueError("Invalid syntax in boolean expression")
    except NameError:
        raise ValueError("Undefined variable in boolean expression")
    except ZeroDivisionError:
        raise ValueError("Division by zero in boolean expression")
    except Exception as e:
        raise ValueError(f"Error evaluating boolean expression: {e}")

if __name__ == '__main__':
    expr1 = "True and False"
    expr2 = "10 > 5 or 1 == 1"
    expr3 = "not (1 == 1)"
    expr4 = "True or False and False"
    print(evaluate_boolean_expression(expr1))
    print(evaluate_boolean_expression(expr2))
    print(evaluate_boolean_expression(expr3))
    print(evaluate_boolean_expression(expr4))