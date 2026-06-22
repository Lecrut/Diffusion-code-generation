def evaluate_expression(expression):
    tokens = []
    current = ""
    i = 0
    while i < len(expression):
        char = expression[i]
        if char == ' ':
            if current:
                tokens.append(current)
                current = ""
        elif char in ('(', ')'):
            if current:
                tokens.append(current)
                current = ""
            tokens.append(char)
        else:
            current += char
        i += 1
    if current:
        tokens.append(current)
    
    def parse_or(index):
        left, index = parse_and(index)
        while index < len(tokens) and tokens[index] == 'OR':
            index += 1
            right, index = parse_and(index)
            left = left or right
        return left, index
    
    def parse_and(index):
        left, index = parse_not(index)
        while index < len(tokens) and tokens[index] == 'AND':
            index += 1
            right, index = parse_not(index)
            left = left and right
        return left, index
    
    def parse_not(index):
        if index < len(tokens) and tokens[index] == 'NOT':
            index += 1
            value, index = parse_not(index)
            return not value, index
        return parse_primary(index)
    
    def parse_primary(index):
        if index < len(tokens) and tokens[index] == '(':
            index += 1
            value, index = parse_or(index)
            if index < len(tokens) and tokens[index] == ')':
                index += 1
            return value, index
        value_str = tokens[index]
        index += 1
        if value_str == 'TRUE':
            return True, index
        elif value_str == 'FALSE':
            return False, index
        else:
            raise ValueError(f"Unknown token: {value_str}")
    
    result, _ = parse_or(0)
    return result

if __name__ == '__main__':
    expressions = [
        "TRUE AND FALSE OR TRUE",
        "NOT TRUE AND FALSE",
        "TRUE OR FALSE AND FALSE",
        "(TRUE OR FALSE) AND FALSE",
        "NOT (TRUE AND FALSE)",
        "TRUE AND (FALSE OR TRUE)",
        "NOT NOT TRUE",
        "FALSE OR FALSE OR TRUE"
    ]
    for expr in expressions:
        result = evaluate_expression(expr)
        print(f"{expr} = {result}")