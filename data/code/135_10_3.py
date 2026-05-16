def are_logically_equivalent(expr1, expr2):
    truth_values = [False, True]
    results = []
    for v1 in truth_values:
        for v2 in truth_values:
            try:
                result1 = eval(f"({expr1.replace('True', str(v1)).replace('False', str(v1))})")
                result2 = eval(f"({expr2.replace('True', str(v2)).replace('False', str(v2))})")
                results.append(result1 == result2)
            except Exception:
                results.append(False)
    return all(results)
if __name__ == '__main__':
    expression1 = "A and B"
    expression2 = "(A and B)"
    print(f"Expression 1: {expression1}")
    print(f"Expression 2: {expression2}")
    print(f"Are they logically equivalent? {are_logically_equivalent(expression1, expression2)}")
    expression3 = "A or B"
    expression4 = "(A or B)"
    print(f"\nExpression 3: {expression3}")
    print(f"Expression 4: {expression4}")
    print(f"Are they logically equivalent? {are_logically_equivalent(expression3, expression4)}")
    expression5 = "True"
    expression6 = "True"
    print(f"\nExpression 5: {expression5}")
    print(f"Expression 6: {expression6}")
    print(f"Are they logically equivalent? {are_logically_equivalent(expression5, expression6)}")
    expression7 = "False"
    expression8 = "False"
    print(f"\nExpression 7: {expression7}")
    print(f"Expression 8: {expression8}")
    print(f"Are they logically equivalent? {are_logically_equivalent(expression7, expression8)}")
    expression9 = "A"
    expression10 = "A"
    print(f"\nExpression 9: {expression9}")
    print(f"Expression 10: {expression10}")
    print(f"Are they logically equivalent? {are_logically_equivalent(expression9, expression10)}")
    expression11 = "A"
    expression12 = "B"
    print(f"\nExpression 11: {expression11}")
    print(f"Expression 12: {expression12}")
    print(f"Are they logically equivalent? {are_logically_equivalent(expression11, expression12)}")