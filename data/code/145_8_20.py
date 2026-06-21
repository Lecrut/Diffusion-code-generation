def evaluate_logical_expression(expression: str, values: list) -> bool:
    tokens = expression.split()
    if not tokens:
        raise ValueError("Empty expression")
    
    values_map = {f'v{i}': val for i, val in enumerate(values)}
    
    def is_operator(token):
        return token in ('and', 'or')
    
    def evaluate_term(tokens_list: list) -> (bool, list):
        if not tokens_list:
            raise ValueError("Empty term")
        
        value = None
        while tokens_list and not is_operator(tokens_list[-1]):
            token = tokens_list.pop()
            value = values_map[token] if isinstance(token, str) else token
        
        operator = tokens_list.pop() if tokens_list else 'and'
        
        result = True
        for term in tokens_list:
            sub_value, _ = evaluate_term([term])
            if operator == 'and':
                result &= sub_value
            elif operator == 'or':
                result |= sub_value
            else:
                raise ValueError(f"Invalid operator: {operator}")
        
        return value and result if value is not None else result
    
    return evaluate_term(tokens)

if __name__ == '__main__':
    sample_values = [True, False, True]
    sample_expression = "v0 and v1 or v2"
    print(evaluate_logical_expression(sample_expression, sample_values))