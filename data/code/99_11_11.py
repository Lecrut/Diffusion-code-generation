def evaluate_nested_conditions(conditions):
    if not conditions:
        return False
    tokens = []
    for cond in conditions:
        if isinstance(cond, bool):
            tokens.append(('VALUE', cond))
        elif isinstance(cond, str):
            if cond.upper() == 'NOT':
                tokens.append(('NOT', None))
            elif cond.upper() == 'AND':
                tokens.append(('AND', None))
            elif cond.upper() == 'OR':
                tokens.append(('OR', None))
            else:
                raise ValueError(f'Unsupported condition: {cond}')
        else:
            raise ValueError(f'Unsupported condition type: {type(cond)}')
    if len(tokens) == 1 and tokens[0][0] == 'VALUE':
        return tokens[0][1]
    processed_tokens = []
    i = 0
    while i < len(tokens):
        if tokens[i][0] == 'NOT':
            if i + 1 < len(tokens) and tokens[i + 1][0] == 'VALUE':
                processed_tokens.append(('VALUE', not tokens[i + 1][1]))
                i += 2
            else:
                raise ValueError('NOT operator must be followed by a value')
        else:
            processed_tokens.append(tokens[i])
            i += 1
    tokens = processed_tokens
    processed_tokens = []
    i = 0
    while i < len(tokens):
        if tokens[i][0] == 'AND':
            if i > 0 and i + 1 < len(tokens) and (tokens[i - 1][0] == 'VALUE') and (tokens[i + 1][0] == 'VALUE'):
                left_val = tokens[i - 1][1]
                right_val = tokens[i + 1][1]
                result = left_val and right_val
                processed_tokens.pop()
                processed_tokens.append(('VALUE', result))
                i += 2
            else:
                raise ValueError('AND operator must be between two values')
        else:
            processed_tokens.append(tokens[i])
            i += 1
    tokens = processed_tokens
    result = False
    if len(tokens) == 1 and tokens[0][0] == 'VALUE':
        result = tokens[0][1]
    else:
        i = 0
        while i < len(tokens):
            if tokens[i][0] == 'OR':
                if i > 0 and i + 1 < len(tokens) and (tokens[i - 1][0] == 'VALUE') and (tokens[i + 1][0] == 'VALUE'):
                    left_val = tokens[i - 1][1]
                    right_val = tokens[i + 1][1]
                    result = left_val or right_val
                    processed_tokens.pop()
                    processed_tokens.append(('VALUE', result))
                    i += 2
                else:
                    raise ValueError('OR operator must be between two values')
            else:
                processed_tokens.append(tokens[i])
                i += 1
        if len(processed_tokens) == 1 and processed_tokens[0][0] == 'VALUE':
            result = processed_tokens[0][1]
        else:
            raise ValueError('Invalid expression after processing')
    return result
if __name__ == '__main__':
    result1 = evaluate_nested_conditions([True, 'AND', False])
    print(result1)
    result2 = evaluate_nested_conditions([False, 'OR', True])
    print(result2)
    result3 = evaluate_nested_conditions([True, 'OR', False, 'AND', False])