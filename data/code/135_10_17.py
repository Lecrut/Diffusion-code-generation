def are_logically_equivalent(expr1, expr2):
    inputs = [(False, False), (False, True), (True, False), (True, True)]
    for a, b in inputs:
        result1 = eval(expr1, {"__builtins__": None}, {"a": a, "b": b})
        result2 = eval(expr2, {"__builtins__": None}, {"a": a, "b": b})
        if result1 != result2:
            return False
    return True

if __name__ == '__main__':
    expression1 = "a and b"
    expression2 = "a + b"
    print(f"Expression 1: {expression1}")
    print(f"Expression 2: {expression2}")
    print(f"Are they logically equivalent? {are_logically_equivalent(expression1, expression2)}")
    
    expression3 = "a == b"
    expression4 = "(a == b)"
    print(f"\nExpression 3: {expression3}")
    print(f"Expression 4: {expression4}")
    print(f"Are they logically equivalent? {are_logically_equivalent(expression3, expression4)}")