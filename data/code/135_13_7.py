import ast
def evaluate_expression(expression, context):
    if isinstance(expression, str):
        if expression == 'True':
            return True
        elif expression == 'False':
            return False
        elif expression == 'and':
            return context['left'] and context['right']
        elif expression == 'or':
            return context['left'] or context['right']
        elif expression == 'not':
            return not context['left']
        else:
            raise ValueError(f"Unknown string expression: {expression}")
    elif isinstance(expression, bool):
        return expression
    else:
        raise TypeError("Unsupported expression type")
def safe_eval(expression, context):
    if isinstance(expression, str):
        try:
            if expression == 'True':
                return True
            elif expression == 'False':
                return False
            elif expression == 'and':
                return context['left'] and context['right']
            elif expression == 'or':
                return context['left'] or context['right']
            elif expression == 'not':
                return not context['left']
            else:
                return bool(eval(expression, {}, context))
        except Exception as e:
            raise ValueError(f"Error evaluating string expression '{expression}': {e}")
    elif isinstance(expression, bool):
        return expression
    else:
        raise TypeError("Input must be a string or boolean")
def compare_boolean_expressions(expr1_str, expr2_str):
    context = {}
    try:
        val1 = safe_eval(expr1_str, context)
        val2 = safe_eval(expr2_str, context)
        return val1 == val2
    except (ValueError, TypeError) as e:
        return f"Error during evaluation: {e}"
if __name__ == '__main__':
    expression1 = "True"
    expression2 = "True"
    result1 = compare_boolean_expressions(expression1, expression2)
    print(f"Expression 1: {expression1}, Expression 2: {expression2}, Same Truth Value: {result1}")
    expression1 = "True"
    expression2 = "False"
    result2 = compare_boolean_expressions(expression1, expression2)
    print(f"Expression 1: {expression1}, Expression 2: {expression2}, Same Truth Value: {result2}")
    expression1 = "True"
    expression2 = "False"
    result3 = compare_boolean_expressions(expression1, expression2)
    print(f"Expression 1: {expression1}, Expression 2: {expression2}, Same Truth Value: {result3}")
    expression1 = "False"
    expression2 = "False"
    result4 = compare_boolean_expressions(expression1, expression2)
    print(f"Expression 1: {expression1}, Expression 2: {expression2}, Same Truth Value: {result4}")
    expression1 = "and"
    expression2 = "True"
    result5 = compare_boolean_expressions(expression1, expression2)
    print(f"Expression 1: {expression1}, Expression 2: {expression2}, Same Truth Value: {result5}")
    expression1 = "True and False"
    expression2 = "False"
    result6 = compare_boolean_expressions(expression1, expression2)
    print(f"Expression 1: {expression1}, Expression 2: {expression2}, Same Truth Value: {result6}")