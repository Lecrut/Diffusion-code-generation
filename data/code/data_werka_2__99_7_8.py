def evaluate_boolean_expression(expression: str) -> bool:
    try:
        sanitized = expression.strip()
        if not sanitized:
            raise ValueError("Empty expression")
        
        result = eval(sanitized, {"__builtins__": {}}, {})
        
        if not isinstance(result, bool):
            raise ValueError(f"Expression did not evaluate to a boolean, got {type(result)}")
            
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
    expr1 = "True and False"
    expr2 = "10 > 5 or 1 == 2"
    expr3 = "not (5 < 3)"
    expr4 = "2 + 2 == 4 and 10 / 2 == 5"
    
    print(evaluate_boolean_expression(expr1))
    print(evaluate_boolean_expression(expr2))
    print(evaluate_boolean_expression(expr3))
    print(evaluate_boolean_expression(expr4))