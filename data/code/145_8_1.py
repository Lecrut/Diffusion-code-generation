def evaluate_boolean_expression(expression, values):
    tokens = expression.split()
    if not tokens:
        raise ValueError("Empty expression")
    values_map = {}
    for i, val in enumerate(values):
        values_map[f'v{i}'] = val
    def evaluate_term(tokens_list):
        if not tokens_list:
            return None, []
        if len(tokens_list) == 1:
            token = tokens_list[0]
            if token in values_map:
                return values_map[token], []
            else:
                raise NameError(f"Undefined variable or constant: {token}")
        if tokens_list[0] in ('True', 'False'):
            return tokens_list.pop(0), tokens_list
        precedence = {'!': 3, 'and': 2, 'or': 1}
        return evaluate_tokens_recursive(tokens, values_map)
    def evaluate_tokens_recursive(tokens_list, values_map):
        if not tokens_list:
            return None
        token = tokens_list[0]
        if token in values_map:
            return values_map[token]
        if token in ('True', 'False'):
            return token == 'True'
        if token == 'not':
            if len(tokens_list) < 2:
                raise ValueError("Syntax error: 'not' requires an operand")
            operand_result = evaluate_tokens_recursive(tokens_list[1:], values_map)
            return not operand_result
        try:
            return eval(expression, {}, values_map)
        except Exception as e:
            raise ValueError(f"Error during evaluation: {e}")
    return evaluate_tokens_recursive(tokens, values_map)
if __name__ == '__main__':
    expression1 = "v0 and v1 or not v2"
    values1 = ['True', 'False', 'True']
    result1 = evaluate_boolean_expression(expression1, values1)
    print(f"Expression: {expression1}, Values: {values1}")
    print(f"Result: {result1}\n")
    expression2 = "(v0 and v1) or (not v2)"
    values2 = ['True', 'True', 'False']
    result2 = evaluate_boolean_expression(expression2, values2)
    print(f"Expression: {expression2}, Values: {values2}")
    print(f"Result: {result2}\n")
    expression3 = "v0 and (v1 or v2)"
    values3 = ['True', 'False', 'True']
    result3 = evaluate_boolean_expression(expression3, values3)
    print(f"Expression: {expression3}, Values: {values3}")
    print(f"Result: {result3}\n")
    expression4 = "not (v0 and v1)"
    values4 = ['True', 'True']
    result4 = evaluate_boolean_expression(expression4, values4)
    print(f"Expression: {expression4}, Values: {values4}")
    print(f"Result: {result4}\n")