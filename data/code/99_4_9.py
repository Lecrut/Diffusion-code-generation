def evaluate_expression(expression: str) -> float:
    if not expression or not expression.strip():
        raise ValueError("Empty expression")
    
    def parse():
        result = parse_term()
        return result
    
    def parse_term():
        result = parse_factor()
        while pos[0] < len(tokens) and tokens[pos[0]] in ('+', '-'):
            op = tokens[pos[0]]
            pos[0] += 1
            right = parse_factor()
            if op == '+':
                result += right
            else:
                result -= right
        return result
    
    def parse_factor():
        result = parse_power()
        while pos[0] < len(tokens) and tokens[pos[0]] in ('*', '/'):
            op = tokens[pos[0]]
            pos[0] += 1
            right = parse_power()
            if op == '*':
                result *= right
            else:
                if right == 0:
                    raise ValueError("Division by zero")
                result /= right
        return result
    
    def parse_power():
        result = parse_primary()
        if pos[0] < len(tokens) and tokens[pos[0]] == '^':
            pos[0] += 1
            exponent = parse_power()
            result = result ** exponent
        return result
    
    def parse_primary():
        if pos[0] < len(tokens):
            token = tokens[pos[0]]
            if token == '(':
                pos[0] += 1
                result = parse_term()
                if pos[0] < len(tokens) and tokens[pos[0]] == ')':
                    pos[0] += 1
                else:
                    raise ValueError("Missing closing parenthesis")
                return result
            if token == '-':
                pos[0] += 1
                return -parse_primary()
            if token == '+':
                pos[0] += 1
                return parse_primary()
            if isinstance(token, (int, float)):
                pos[0] += 1
                return token
        raise ValueError("Unexpected end of expression")
    
    tokens = []
    i = 0
    length = len(expression)
    while i < length:
        char = expression[i]
        if char.isspace():
            i += 1
            continue
        if char in '()':
            tokens.append(char)
            i += 1
            continue
        if char in '+-*/^':
            tokens.append(char)
            i += 1
            continue
        if char.isdigit() or char == '.':
            num_str = ""
            while i < length and (expression[i].isdigit() or expression[i] == '.'):
                num_str += expression[i]
                i += 1
            if '.' in num_str:
                tokens.append(float(num_str))
            else:
                tokens.append(int(num_str))
            continue
        raise ValueError(f"Invalid character: {char}")
    
    pos = [0]
    result = parse()
    return result

if __name__ == '__main__':
    print(evaluate_expression("((2 + 3) * (4 - 1))"))
    print(evaluate_expression("10 / 2"))
    print(evaluate_expression("2 ^ 3"))
    print(evaluate_expression("-5 + 10"))
    print(evaluate_expression("  100  "))