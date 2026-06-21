TRUE_VALUE = True
FALSE_VALUE = False
NOT_OPERATOR = "NOT"
AND_OPERATOR = "AND"
OR_OPERATOR = "OR"
OPEN_PAREN = "("
CLOSE_PAREN = ")"

def evaluate_boolean_expression(expression: str) -> bool:
    tokens = expression.split()
    normalized_tokens = []
    for token in tokens:
        upper_token = token.upper()
        if upper_token == "TRUE":
            normalized_tokens.append(TRUE_VALUE)
        elif upper_token == "FALSE":
            normalized_tokens.append(FALSE_VALUE)
        elif upper_token == NOT_OPERATOR:
            normalized_tokens.append(NOT_OPERATOR)
        elif upper_token == AND_OPERATOR:
            normalized_tokens.append(AND_OPERATOR)
        elif upper_token == OR_OPERATOR:
            normalized_tokens.append(OR_OPERATOR)
        elif token == OPEN_PAREN:
            normalized_tokens.append(OPEN_PAREN)
        elif token == CLOSE_PAREN:
            normalized_tokens.append(CLOSE_PAREN)
        else:
            raise ValueError(f"Unknown token: {token}")
    result, _ = _parse_or(normalized_tokens, 0)
    return result

def _parse_or(tokens: list, index: int):
    left, index = _parse_and(tokens, index)
    while index < len(tokens) and tokens[index] == OR_OPERATOR:
        index += 1
        right, index = _parse_and(tokens, index)
        left = left or right
    return left, index

def _parse_and(tokens: list, index: int):
    left, index = _parse_not(tokens, index)
    while index < len(tokens) and tokens[index] == AND_OPERATOR:
        index += 1
        right, index = _parse_not(tokens, index)
        left = left and right
    return left, index

def _parse_not(tokens: list, index: int):
    if index < len(tokens) and tokens[index] == NOT_OPERATOR:
        index += 1
        val, index = _parse_not(tokens, index)
        return not val, index
    return _parse_primary(tokens, index)

def _parse_primary(tokens: list, index: int):
    if index < len(tokens) and tokens[index] == OPEN_PAREN:
        index += 1
        val, index = _parse_or(tokens, index)
        if index < len(tokens) and tokens[index] == CLOSE_PAREN:
            index += 1
            return val, index
        raise ValueError("Missing closing parenthesis")
    if index < len(tokens) and isinstance(tokens[index], bool):
        return tokens[index], index + 1
    raise ValueError("Expected boolean value or parenthesis")

if __name__ == '__main__':
    expr1 = "True AND False OR True"
    result1 = evaluate_boolean_expression(expr1)
    print(result1)

    expr2 = "(True OR False) AND NOT False"
    result2 = evaluate_boolean_expression(expr2)
    print(result2)

    expr3 = "NOT (True AND False)"
    result3 = evaluate_boolean_expression(expr3)
    print(result3)