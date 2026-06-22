def evaluate_expression(expression: str) -> bool:
    tokens = expression.replace('(', ' ( ').replace(')', ' ) ').split()
    precedence = {'NOT': 3, 'AND': 2, 'OR': 1}
    values = {'true': True, 'false': False}
    
    def parse_expr(index):
        left = parse_term(index)
        current_index = left[0]
        result = left[1]
        
        while current_index < len(tokens) and tokens[current_index] in ('OR',):
            op = tokens[current_index]
            current_index += 1
            right = parse_term(current_index)
            current_index = right[0]
            if op == 'OR':
                result = result or right[1]
            current_index += 1
        return current_index, result

    def parse_term(index):
        left = parse_factor(index)
        current_index = left[0]
        result = left[1]
        
        while current_index < len(tokens) and tokens[current_index] in ('AND',):
            op = tokens[current_index]
            current_index += 1
            right = parse_factor(current_index)
            current_index = right[0]
            if op == 'AND':
                result = result and right[1]
            current_index += 1
        return current_index, result

    def parse_factor(index):
        token = tokens[index]
        if token == '(':
            current_index, result = parse_expr(index + 1)
            if current_index < len(tokens) and tokens[current_index] == ')':
                return current_index + 1, result
            return current_index, result
        if token == 'NOT':
            current_index, result = parse_factor(index + 1)
            return current_index, not result
        if token.lower() in values:
            return index + 1, values[token.lower()]
        raise ValueError(f"Unknown token: {token}")

    _, result = parse_expr(0)
    return result

if __name__ == '__main__':
    expressions = [
        "true AND false OR true",
        "true OR false AND false",
        "NOT true AND false",
        "(true OR false) AND NOT false",
        "NOT (true AND false) OR false"
    ]
    for expr in expressions:
        print(evaluate_expression(expr))