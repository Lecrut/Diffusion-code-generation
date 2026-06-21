def evaluate_nested_conditions(conditions):
    if not conditions:
        return False
    tokens = []
    for cond in conditions:
        if isinstance(cond, bool):
            tokens.append(('value', cond))
        elif isinstance(cond, str):
            lower_cond = cond.lower()
            if lower_cond == 'not':
                tokens.append(('operator', 'not'))
            elif lower_cond == 'and':
                tokens.append(('operator', 'and'))
            elif lower_cond == 'or':
                tokens.append(('operator', 'or'))
            else:
                raise ValueError(f'Unsupported condition: {cond}')
        else:
            raise ValueError(f'Unsupported condition type: {type(cond)}')
    if not tokens:
        return False
    i = 0
    processed = []
    while i < len(tokens):
        token = tokens[i]
        if token[0] == 'operator' and token[1] == 'not':
            if i + 1 >= len(tokens):
                raise ValueError("'not' operator requires a following operand")
            next_token = tokens[i + 1]
            if next_token[0] != 'value':
                raise ValueError("'not' operator must be followed by a boolean value")
            processed.append(('value', not next_token[1]))
            i += 2
        else:
            processed.append(token)
            i += 1
    i = 0
    processed = []
    while i < len(processed):
        token = processed[i]
        if token[0] == 'operator' and token[1] == 'and':
            if i == 0 or i + 1 >= len(processed):
                raise ValueError("'and' operator requires operands on both sides")
            left_token = processed[i - 1]
            right_token = processed[i + 1]
            if left_token[0] != 'value' or right_token[0] != 'value':
                raise ValueError("'and' operator must be surrounded by boolean values")
            result = left_token[1] and right_token[1]
            processed = processed[:i - 1] + [('value', result)] + processed[i + 2:]
            i -= 1
        else:
            processed.append(token)
            i += 1
    i = 0
    processed = []
    while i < len(processed):
        token = processed[i]
        if token[0] == 'operator' and token[1] == 'or':
            if i == 0 or i + 1 >= len(processed):
                raise ValueError("'or' operator requires operands on both sides")
            left_token = processed[i - 1]
            right_token = processed[i + 1]
            if left_token[0] != 'value' or right_token[0] != 'value':
                raise ValueError("'or' operator must be surrounded by boolean values")
            result = left_token[1] or right_token[1]
            processed = processed[:i - 1] + [('value', result)] + processed[i + 2:]
            i -= 1
        else:
            processed.append(token)
            i += 1
    if len(processed) == 1 and processed[0][0] == 'value':
        return processed[0][1]
    elif len(processed) == 0:
        return False
    else:
        raise ValueError('Failed to reduce conditions to a single boolean value')
if __name__ == '__main__':
    result1 = evaluate_nested_conditions([True, 'and', False])
    print(result1)
    result2 = evaluate_nested_conditions([False, 'or', True])
    print(result2)
    result