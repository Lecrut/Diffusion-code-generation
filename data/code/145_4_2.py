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
        elif len(results) > 1:
            return all(results)
        else:
            return False
    else:
        return expression
if __name__ == '__main__':
    expression1 = [True, False]
    print(evaluate_nested_boolean(expression1))
    expression2 = [[True, [False, True]], [True]]
    print(evaluate_nested_boolean(expression2))
    expression3 = [True, [False, [True, False]]]
    print(evaluate_nested_boolean(expression3))
    expression4 = [True, [False, [True, [False, True]]]]
    print(evaluate_nested_boolean(expression4))
    expression5 = [[True, [False, [True, [False, [True, False]]]]]]
    print(evaluate_nested_boolean(expression5))