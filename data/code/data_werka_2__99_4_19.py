def parse_expression(expr):
    def helper(index):
        left, index = parse_term(index)
        while index < len(expr) and expr[index] in ('+', '-'):
            op = expr[index]
            index += 1
            right, index = parse_term(index)
            if op == '+':
                left = left + right
            else:
                left = left - right
        return left, index

    def parse_term(index):
        left, index = parse_factor(index)
        while index < len(expr) and expr[index] in ('*', '/'):
            op = expr[index]
            index += 1
            right, index = parse_factor(index)
            if op == '*':
                left = left * right
            else:
                if right == 0:
                    raise ValueError("Division by zero")
                left = left / right
        return left, index

    def parse_factor(index):
        if index >= len(expr):
            raise ValueError("Unexpected end of expression")
        
        if expr[index] == '(':
            index += 1
            value, index = helper(index)
            if index >= len(expr) or expr[index] != ')':
                raise ValueError("Missing closing parenthesis")
            index += 1
            return value, index
        elif expr[index] == '-':
            index += 1
            value, index = parse_factor(index)
            return -value, index
        elif expr[index].isdigit() or expr[index] == '.':
            start = index
            while index < len(expr) and (expr[index].isdigit() or expr[index] == '.'):
                index += 1
            num_str = expr[start:index]
            if '.' in num_str:
                return float(num_str), index
            else:
                return int(num_str), index
        else:
            raise ValueError(f"Unexpected character: {expr[index]}")

    expr = expr.replace(' ', '')
    if not expr:
        raise ValueError("Empty expression")
    
    result, end_index = helper(0)
    if end_index != len(expr):
        raise ValueError("Unexpected characters at end of expression")
    
    return result

if __name__ == '__main__':
    print(parse_expression("((1+2)*(3+4))"))
    print(parse_expression("((10/2)-3)"))
    print(parse_expression("((5+((3*2)-1)))"))
    print(parse_expression("-((2+3))"))