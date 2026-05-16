def are_logically_equivalent(expr1, expr2):
    truth_values = [False, True]
    results = []
    for v1 in truth_values:
        for v2 in truth_values:
            result1 = eval(f"({expr1})") if isinstance(expr1, str) else expr1
            result2 = eval(f"({expr2})") if isinstance(expr2, str) else expr2
            try:
                val1 = eval(f"({expr1})")
            except:
                val1 = expr1
            try:
                val2 = eval(f"({expr2})")
            except:
                val2 = expr2
            results.append(val1 == val2)
    return all(results)
if __name__ == '__main__':
    expression1 = "True or False"
    expression2 = "False or True"
    print(f"Expression 1: {expression1}")
    print(f"Expression 2: {expression2}")
    equivalence = are_logically_equivalent(expression1, expression2)
    print(f"Are the expressions logically equivalent? {equivalence}")
    expression3 = "not (True and False)"
    expression4 = "False"
    print(f"\nExpression 3: {expression3}")
    print(f"Expression 4: {expression4}")
    equivalence2 = are_logically_equivalent(expression3, expression4)
    print(f"Are the expressions logically equivalent? {equivalence2}")