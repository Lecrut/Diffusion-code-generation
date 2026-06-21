def evaluate_boolean_expression(expression: str) -> bool:
    try:
        result = eval(expression, {"__builtins__": {}}, {})
        if not isinstance(result, bool):
            raise ValueError("Expression did not evaluate to a boolean")
        return result
    except SyntaxError:
        raise ValueError("Invalid syntax in boolean expression")
    except NameError:
        raise ValueError("Undefined variable in boolean expression")
    except Exception as e:
        raise ValueError(f"Error evaluating expression: {e}")

if __name__ == '__main__':
    expr1 = "True and False"
    expr2 = "10 > 5 or 2 == 3"
    expr3 = "not (1 == 1)"
    expr4 = "5 >= 5 and 3 < 4"
    
    print(evaluate_boolean_expression(expr1))
    print(evaluate_boolean_expression(expr2))
    print(evaluate_boolean_expression(expr3))
    print(evaluate_boolean_expression(expr4))