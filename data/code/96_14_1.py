def evaluate_nested_boolean_expression(expression: str, variables: dict) -> bool:
    stack = []
    tokens = expression.replace('(', ' ( ').replace(')', ' ) ').split()
    for token in tokens:
        if token.isdigit() or token in variables:
            if token.isdigit():
                stack.append(bool(int(token)))
            elif token in variables:
                stack.append(variables[token])
        elif token == '(':
            stack.append(None)
        elif token == ')':
            if not stack:
                raise ValueError("Mismatched parentheses: closing parenthesis without opening one.")
            result = stack.pop()
            if result is None:
                raise ValueError("Mismatched parentheses: empty expression inside parentheses.")
            stack.append(result)
        else:
            if token.lower() == 'and':
                if len(stack) < 2:
                    raise ValueError("Syntax error: 'and' requires two operands.")
                right = stack.pop()
                left = stack.pop()
                stack.append(left and right)
            elif token.lower() == 'or':
                if len(stack) < 2:
                    raise ValueError("Syntax error: 'or' requires two operands.")
                right = stack.pop()
                left = stack.pop()
                stack.append(left or right)
            else:
                raise ValueError(f"Unknown token: {token}")
    if len(stack) != 1:
        raise ValueError("Syntax error: Unbalanced expression.")
    return stack[0]
if __name__ == '__main__':
    variables = {
        "A": True,
        "B": False,
        "C": True
    }
    test_cases = [
        ("A and (B or C)", variables, True),
        ("(A and B) or C", variables, True),
        ("not (A or B)", variables, False),
        ("A and not B", variables, False),
        ("not (A and B)", variables, False),
        ("A or (B and C)", variables, True),
        ("A and (B or (C and A))", variables, True),
        ("A and (B or (C and D))", variables, False)                                                                                                                                                
    ]
    print("--- Testing Nested Expression Evaluation ---")
    for expression, vars_dict, expected in test_cases:
        try:
            result = evaluate_nested_boolean_expression(expression, vars_dict)
            status = "PASS" if result == expected else f"FAIL (Expected: {expected}, Got: {result})"
            print(f"Expression: '{expression}'")
            print(f"Result: {result} | Status: {status}\n")
        except ValueError as e:
            print(f"Expression: '{expression}'")
            print(f"ERROR: {e}\n")
        except Exception as e:
            print(f"Expression: '{expression}'")
            print(f"UNEXPECTED ERROR: {e}\n")
    print("--- Testing Error Handling ---")
    error_cases = [
        ("A and B", variables, None),                                       
        ("(A and B", variables, None),             
        ("A and", variables, None),                  
        ("A or B or C", variables, None),                                      
        ("A & B", variables, None)                   
    ]
    for expression, vars_dict, _ in error_cases:
        try:
            evaluate_nested_boolean_expression(expression, vars_dict)
            print(f"Expression: '{expression}' | FAILED TO CATCH ERROR")
        except ValueError as e:
            print(f"Expression: '{expression}' | Successfully caught error: {e}\n")
        except Exception as e:
            print(f"Expression: '{expression}' | Caught unexpected error: {e}\n")