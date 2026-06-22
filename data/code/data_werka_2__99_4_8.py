def parse_expression(expr: str) -> float:
    expr = expr.replace(' ', '')
    if not expr:
        raise ValueError('Empty expression')

    def parse_term(start: int) -> tuple:
        val, end = parse_factor(start)
        while end < len(expr) and expr[end] in ('*', '/'):
            op = expr[end]
            next_val, end = parse_factor(end + 1)
            if op == '*':
                val *= next_val
            else:
                if next_val == 0:
                    raise ValueError('Division by zero')
                val /= next_val
        return (val, end)

    def parse_factor(start: int) -> tuple:
        if start >= len(expr):
            raise ValueError('Unexpected end of expression')
        if expr[start] == '(':
            val, end = parse_expression(expr[start + 1:])
            if end + 1 >= len(expr) or expr[end + 1] != ')':
                raise ValueError('Missing closing parenthesis')
            return (val, end + 2)
        if expr[start] == '-':
            val, end = parse_factor(start + 1)
            return (-val, end)
        if expr[start] == '+':
            val, end = parse_factor(start + 1)
            return (val, end)
        end = start
        while end < len(expr) and (expr[end].isdigit() or expr[end] == '.'):
            end += 1
        if end == start:
            raise ValueError(f'Unexpected character at index {start}: {expr[start]}')
        num_str = expr[start:end]
        if '.' in num_str:
            return (float(num_str), end)
        return (int(num_str), end)
    result, end = parse_term(0)
    if end != len(expr):
        raise ValueError(f'Unexpected character at index {end}: {expr[end]}')
    return result
if __name__ == '__main__':
    print(parse_expression('(1 + 2) * (3 + 4)'))
    print(parse_expression('((10 / 2) + (3 * 4)) - 5'))
    print(parse_expression('((2 + 3) * (4 - 1)) / 5'))
    print(parse_expression('1 + 2 * 3'))
    print(parse_expression('((10 + 5) / 3)'))