def evaluate_nested_boolean(expression):
    if isinstance(expression, bool):
        return expression
    elif isinstance(expression, list) or isinstance(expression, tuple):
        if not expression:
            return False
        if len(expression) == 1:
            return evaluate_nested_boolean(expression[0])
        else:
            results = [evaluate_nested_boolean(item) for item in expression]
            if len(results) == 1:
                return results[0]
            elif len(results) == 2:
                return results[0] and results[1]
            else:
                return all(results)
    else:
        return expression
if __name__ == '__main__':
    expression1 = [True, [False, True], True]
    expression2 = (True and [False, True], False)
    expression3 = [[True, False], [True], False]
    expression4 = [True, [False, [True, False]], True]
    expression5 = [True, [False, [True, [False, True]]], True]
    print(f"Expression 1: {evaluate_nested_boolean(expression1)}")
    print(f"Expression 2: {evaluate_nested_boolean(expression2)}")
    print(f"Expression 3: {evaluate_nested_boolean(expression3)}")
    print(f"Expression 4: {evaluate_nested_boolean(expression4)}")
    print(f"Expression 5: {evaluate_nested_boolean(expression5)}")