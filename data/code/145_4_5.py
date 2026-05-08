def evaluate_nested_boolean(expression):
    if isinstance(expression, bool):
        return expression
    elif isinstance(expression, list) or isinstance(expression, tuple):
        if not expression:
            return False
        if all(isinstance(item, list) or isinstance(item, tuple) for item in expression):
            results = [evaluate_nested_boolean(sub_expression) for sub_expression in expression]
            if len(results) == 1:
                return results[0]
            elif len(results) > 1:
                return all(results)
            else:
                return False
        else:
            return any(evaluate_nested_boolean(item) for item in expression)
    else:
        return expression
if __name__ == '__main__':
    expression1 = [True, False]
    print(f"Expression 1: {expression1}, Result: {evaluate_nested_boolean(expression1)}")
    expression2 = [True, True, False]
    print(f"Expression 2: {expression2}, Result: {evaluate_nested_boolean(expression2)}")
    expression3 = [[True, False], [False, True]]
    print(f"Expression 3: {expression3}, Result: {evaluate_nested_boolean(expression3)}")
    expression4 = [[True, [False, True]], [False]]
    print(f"Expression 4: {expression4}, Result: {evaluate_nested_boolean(expression4)}")
    expression5 = [[True, [False, [True, False]]], [True]]
    print(f"Expression 5: {expression5}, Result: {evaluate_nested_boolean(expression5)}")
    expression6 = [True]
    print(f"Expression 6: {expression6}, Result: {evaluate_nested_boolean(expression6)}")
    expression7 = []
    print(f"Expression 7: {expression7}, Result: {evaluate_nested_boolean(expression7)}")