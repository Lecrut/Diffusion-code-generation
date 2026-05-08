def evaluate_boolean_expression(expression, values):
    tokens = expression.split()
    if not tokens:
        raise ValueError("Empty expression")
    values_map = {}
    for i, val in enumerate(values):
        values_map[f"v{i}"] = val
    def evaluate_term(term):
        if term.startswith('v'):
            return values_map[term]
        return term
    def parse_and_evaluate(tokens):
        if not tokens:
            return False
        if tokens[0] in ('True', 'False'):
            return tokens.pop(0) == 'True'
        substituted_expression = expression
        for i, val in enumerate(values):
            substituted_expression = substituted_expression.replace(f"v{i}", str(val))
        try:
            return eval(substituted_expression)
        except Exception as e:
            raise ValueError(f"Error evaluating expression: {substituted_expression}. Error: {e}")
    return parse_and_evaluate(tokens)
if __name__ == '__main__':
    values = [True, False, True]
    expression1 = "v0 and v1"
    result1 = evaluate_boolean_expression(expression1, values)
    print(f"Expression: {expression1}, Values: {values}, Result: {result1}")
    expression2 = "(v0 or v1) and v2"
    result2 = evaluate_boolean_expression(expression2, values)
    print(f"Expression: {expression2}, Values: {values}, Result: {result2}")
    expression3 = "not (v0 and v2) or v1"
    result3 = evaluate_boolean_expression(expression3, values)
    print(f"Expression: {expression3}, Values: {values}, Result: {result3}")
    expression4 = "v0 and (v1 or (v2 and v0))"
    result4 = evaluate_boolean_expression(expression4, values)
    print(f"Expression: {expression4}, Values: {values}, Result: {result4}")