def evaluate_nested_boolean(expression):
    if isinstance(expression, bool):
        return expression
    elif isinstance(expression, list) or isinstance(expression, tuple):
        if not expression:
            return False
        results = []
        for item in expression:
            result = evaluate_nested_boolean(item)
            results.append(result)
        if len(results) == 1:
            return results[0]
        elif len(results) == 2:
            return results[0] and results[1]
        else:
            return all(results)
    else:
        return expression
if __name__ == '__main__':
    expression1 = [True, False]
    print(f"Expression 1: {expression1}, Result: {evaluate_nested_boolean(expression1)}")
    expression2 = [True, True, False]
    print(f"Expression 2: {expression2}, Result: {evaluate_nested_boolean(expression2)}")
    expression3 = [True, True, True]
    print(f"Expression 3: {expression3}, Result: {evaluate_nested_boolean(expression3)}")
    expression4 = [False]
    print(f"Expression 4: {expression4}, Result: {evaluate_nested_boolean(expression4)}")
    expression5 = [True, [False, True], False]
    print(f"Expression 5: {expression5}, Result: {evaluate_nested_boolean(expression5)}")
    expression6 = [[True, [False, True]], False]
    print(f"Expression 6: {expression6}, Result: {evaluate_nested_boolean(expression6)}")
    expression7 = [True, [False, [True, False]], True]
    print(f"Expression 7: {expression7}, Result: {evaluate_nested_boolean(expression7)}")