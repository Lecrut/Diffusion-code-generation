def evaluate_boolean_expression(expression: str) -> bool:
    if not isinstance(expression, str):
        raise TypeError("Expression must be a string")
    
    cleaned = expression.strip()
    if not cleaned:
        raise ValueError("Empty expression provided")
    
    if not all(c not in cleaned for c in ['{', '}', '[', ']', ';', ':']):
        raise ValueError("Unsupported characters in expression")
    
    try:
        allowed_globals = {
            "True": True,
            "False": False,
            "and": lambda x, y: x and y,
            "or": lambda x, y: x or y,
            "not": lambda x: not x,
            "is": lambda x, y: x is y,
            "in": lambda x, y: x in y,
            "None": None,
        }
        
        allowed_builtins = {}
        
        result = eval(cleaned, {"__builtins__": allowed_builtins}, allowed_globals)
        
        if isinstance(result, bool):
            return result
        elif result is True or result is False:
            return result
        else:
            raise ValueError("Result is not a boolean")
            
    except SyntaxError:
        raise ValueError("Syntax error in boolean expression")
    except NameError:
        raise ValueError("Undefined variable or keyword in expression")
    except ZeroDivisionError:
        raise ValueError("Division by zero in expression")
    except Exception as e:
        raise ValueError(f"Error evaluating expression: {e}")

if __name__ == '__main__':
    test_cases = [
        "True and False",
        "10 > 5 or 1 == 1",
        "not (1 == 1)",
        "True or False and False",
        "2 + 2 == 4",
    ]
    
    for expr in test_cases:
        print(evaluate_boolean_expression(expr))