def evaluate_nested_boolean(expression):
    if isinstance(expression, bool):
        return expression
    elif isinstance(expression, list) or isinstance(expression, tuple):
        if not expression:
            return False
        if all(isinstance(item, list) or isinstance(item, tuple) for item in expression):
            results = [evaluate_nested_boolean(item) for item in expression]
            if len(results) == 1:
                return results[0]
            elif len(results) > 1:
                return all(results)
            else:
                return False
        else:
            results = [evaluate_nested_boolean(item) for item in expression]
            return all(results)
    else:
        return expression
if __name__ == '__main__':
    expression1 = [[True, False], [True], [False]]
    expression2 = (True, [False, True], True)
    expression3 = [[True, [False, True]], [True]]
    expression4 = [True, False]
    expression5 = [[True, True, [False, False]], [True]]
    expression6 = (True, [False], True)
    print(f"Expression 1: {evaluate_nested_boolean(expression1)}")
    print(f"Expression 2: {evaluate_nested_boolean(expression2)}")
    print(f"Expression 3: {evaluate_nested_boolean(expression3)}")
    print(f"Expression 4: {evaluate_nested_boolean(expression4)}")
    print(f"Expression 5: {evaluate_nested_boolean(expression5)}")
    print(f"Expression 6: {evaluate_nested_boolean(expression6)}")