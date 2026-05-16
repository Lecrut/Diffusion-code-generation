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
    expression4 = "a == b"
    print(f"\nExpression 3: {expression3}")
    print(f"Expression 4: {expression4}")
    print(f"Are they logically equivalent? {are_logically_equivalent(expression3, expression4)}")
    expression5 = "a or b"
    expression6 = "a | b"
    print(f"\nExpression 5: {expression5}")
    print(f"Expression 6: {expression6}")
    print(f"Are they logically equivalent? {are_logically_equivalent(expression5, expression6)}")
    expression7 = "not a"
    expression8 = "not a"
    print(f"\nExpression 7: {expression7}")
    print(f"Expression 8: {expression8}")
    print(f"Are they logically equivalent? {are_logically_equivalent(expression7, expression8)}")
    expression9 = "a and not b"
    expression10 = "not (a or b)"
    print(f"\nExpression 9: {expression9}")
    print(f"Expression 10: {expression10}")
    print(f"Are they logically equivalent? {are_logically_equivalent(expression9, expression10)}")