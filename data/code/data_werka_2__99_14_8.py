def evaluate_boolean_expression(expression: str) -> bool:
    tokens = []
    current_word = []
    for char in expression:
        if char == ' ':
            if current_word:
                tokens.append(''.join(current_word))
                current_word = []
        else:
            current_word.append(char)
    if current_word:
        tokens.append(''.join(current_word))

    def parse_or(index):
        left, index = parse_and(index)
        while index < len(tokens) and tokens[index].upper() == 'OR':
            index += 1
            right, index = parse_and(index)
            left = left or right
        return left, index

    def parse_and(index):
        left, index = parse_not(index)
        while index < len(tokens) and tokens[index].upper() == 'AND':
            index += 1
            right, index = parse_not(index)
            left = left and right
        return left, index

    def parse_not(index):
        if index < len(tokens) and tokens[index].upper() == 'NOT':
            index += 1
            value, index = parse_not(index)
            return not value, index
        return parse_primary(index)

    def parse_primary(index):
        if index >= len(tokens):
            raise ValueError("Unexpected end of expression")
        token = tokens[index]
        if token == '(':
            index += 1
            value, index = parse_or(index)
            if index < len(tokens) and tokens[index] == ')':
                index += 1
            else:
                raise ValueError("Missing closing parenthesis")
            return value, index
        if token.upper() == 'TRUE':
            return True, index + 1
        if token.upper() == 'FALSE':
            return False, index + 1
        raise ValueError(f"Unknown token: {token}")

    result, end_index = parse_or(0)
    if end_index != len(tokens):
        raise ValueError("Unexpected tokens at end of expression")
    return result

if __name__ == '__main__':
    sample_expr = "True AND NOT False OR False"
    result = evaluate_boolean_expression(sample_expr)
    print(result)