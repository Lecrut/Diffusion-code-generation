def parse_expression(s):
    s = s.replace(' ', '')
    if not s:
        raise ValueError("Empty expression")
    
    def parse_add_sub(pos):
        left, pos = parse_mul_div(pos)
        while pos < len(s) and s[pos] in ('+', '-'):
            op = s[pos]
            pos += 1
            right, pos = parse_mul_div(pos)
            if op == '+':
                left = left + right
            else:
                left = left - right
        return left, pos

    def parse_mul_div(pos):
        left, pos = parse_primary(pos)
        while pos < len(s) and s[pos] in ('*', '/'):
            op = s[pos]
            pos += 1
            right, pos = parse_primary(pos)
            if op == '*':
                left = left * right
            else:
                if right == 0:
                    raise ValueError("Division by zero")
                left = left / right
        return left, pos

    def parse_primary(pos):
        if pos >= len(s):
            raise ValueError("Unexpected end of expression")
        
        if s[pos] == '(':
            pos += 1
            result, pos = parse_add_sub(pos)
            if pos >= len(s) or s[pos] != ')':
                raise ValueError("Missing closing parenthesis")
            pos += 1
            return result, pos
        
        if s[pos] == '-':
            pos += 1
            val, pos = parse_primary(pos)
            return -val, pos
        
        if s[pos].isdigit() or s[pos] == '.':
            start = pos
            while pos < len(s) and (s[pos].isdigit() or s[pos] == '.'):
                pos += 1
            num_str = s[start:pos]
            if num_str.count('.') > 1:
                raise ValueError("Invalid number format")
            if '.' in num_str:
                return float(num_str), pos
            return int(num_str), pos
        
        raise ValueError(f"Unexpected character: {s[pos]}")

    result, pos = parse_add_sub(0)
    if pos != len(s):
        raise ValueError(f"Unexpected character at end: {s[pos]}")
    return result

if __name__ == '__main__':
    print(parse_expression("((1+2)*(3-4))"))
    print(parse_expression("((10/2)+5)"))
    print(parse_expression("((2+3)*(4+5))"))
    print(parse_expression("((100-50)/2)"))
    print(parse_expression("((1+2+3)*(4+5+6))"))