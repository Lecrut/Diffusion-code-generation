def evaluate_boolean_expression(expression: str) -> bool:
    if not expression or not expression.strip():
        raise ValueError("Empty expression")
    
    code = compile(expression, "<string>", "eval")
    
    try:
        result = eval(code, {"__builtins__": {}}, {})
    except SyntaxError:
        raise ValueError("Invalid syntax in expression")
    except NameError:
        raise ValueError("Undefined variable in expression")
    except Exception as e:
        raise ValueError(f"Error evaluating expression: {e}")
    
    if not isinstance(result, bool):
        raise ValueError(f"Expression did not evaluate to a boolean, got {type(result)}")
    
    return result

if __name__ == '__main__':
    print(evaluate_boolean_expression("True and False"))
    print(evaluate_boolean_expression("10 > 5 or 1 == 1"))
    print(evaluate_boolean_expression("not (1 == 1)"))
    print(evaluate_boolean_expression("True or False and False"))
    print(evaluate_boolean_expression("5 != 5"))