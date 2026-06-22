def parse_expression(s):
    s = s.strip()
    if not s:
        raise ValueError('Empty expression')

    def parse_addition():
        left = parse_multiplication()
        while True:
            s = s.lstrip()
            if not s:
                break
            if s[0] == '+':
                s = s[1:]
                right = parse_multiplication()
                left = left + right
            elif s[0] == '-':
                s = s[1:]
                right = parse_multiplication()
                left = left - right
            else:
                break
        return left

    def parse_multiplication():
        left = parse_unary()
        while True:
            s = s.lstrip()
            if not s:
                break
            if s[0] == '*':
                s = s[1:]
                right = parse_unary()
                left = left * right
            elif s[0] == '/':
                s = s[1:]
                right = parse_unary()
                if right == 0:
                    raise ValueError('Division by zero')
                left = left / right
            else:
                break
        return left

    def parse_unary():
        s = s.lstrip()
        if not s:
            raise ValueError('Unexpected end of expression')
        if s[0] == '-':
            s = s[1:]
            val = parse_unary()
            return -val
        if s[0] == '+':
            s = s[1:]
            val = parse_unary()
            return val
        return parse_primary()

    def parse_primary():
        s = s.lstrip()
        if not s:
            raise ValueError('Unexpected end of expression')
        if s[0] == '(':
            s = s[1:]
            val = parse_addition()
            s = s.lstrip()
            if not s or s[0] != ')':
                raise ValueError('Missing closing parenthesis')
            s = s[1:]
            return val
        start = 0
        if s[start] == '-':
            start += 1
        if not s[start:].lstrip() or s[start:].lstrip()[0] not in '0123456789.':
            raise ValueError(f'Unexpected character: {s[0]}')
        while start < len(s) and (s[start].isdigit() or s[start] == '.'):
            start += 1
        num_str = s[:start]
        s = s[start:]
        if '.' in num_str:
            return float(num_str)
        return int(num_str)
    result = parse_addition()
    s = s.lstrip()
    if s:
        raise ValueError(f'Unexpected trailing characters: {s}')
    return result
if __name__ == '__main__':
    print(parse_expression('((1 + 2) * (3 + 4))'))
    print(parse_expression('((10 / 2) + (3 * 4))'))
    print(parse_expression('((1 + 2) * ((3 + 4) - 1))'))
    print(parse_expression('-((1 + 2) * 3)'))
    print(parse_expression('((100 / (5 * 2)) + 10)'))