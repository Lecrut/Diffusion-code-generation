import re
import operator

def evaluate_boolean_expression(expression: str, variables: dict) -> bool:
    def parse_expr(tokens, pos):
        val, pos = parse_term(tokens, pos)
        while pos < len(tokens) and tokens[pos] == 'or':
            pos += 1
            right, pos = parse_term(tokens, pos)
            val = val or right
        return val, pos

    def parse_term(tokens, pos):
        val, pos = parse_factor(tokens, pos)
        while pos < len(tokens) and tokens[pos] == 'and':
            pos += 1
            right, pos = parse_factor(tokens, pos)
            val = val and right
        return val, pos

    def parse_factor(tokens, pos):
        if pos >= len(tokens):
            raise ValueError("Unexpected end of expression")
        
        token = tokens[pos]
        
        if token == 'not':
            pos += 1
            val, pos = parse_factor(tokens, pos)
            return not val, pos
        
        if token == '(':
            pos += 1
            val, pos = parse_expr(tokens, pos)
            if pos >= len(tokens) or tokens[pos] != ')':
                raise ValueError("Missing closing parenthesis")
            pos += 1
            return val, pos
        
        if token in ('True', 'False'):
            return token == 'True', pos + 1
        
        if token in variables:
            val = variables[token]
            if not isinstance(val, bool):
                raise ValueError(f"Variable {token} must be boolean")
            return val, pos + 1
        
        raise ValueError(f"Unknown token: {token}")

    cleaned = re.sub(r'\s+', ' ', expression).strip()
    if not cleaned:
        return False
    
    tokens = cleaned.split()
    result, end_pos = parse_expr(tokens, 0)
    if end_pos != len(tokens):
        raise ValueError(f"Unexpected tokens after expression: {tokens[end_pos:]}")
    return result

if __name__ == '__main__':
    expr1 = '((A and B) or C)'
    vars1 = {'A': True, 'B': False, 'C': True}
    print(evaluate_boolean_expression(expr1, vars1))
    
    expr2 = 'not (A or B)'
    vars2 = {'A': False, 'B': False}
    print(evaluate_boolean_expression(expr2, vars2))
    
    expr3 = 'A and B and C'
    vars3 = {'A': True, 'B': True, 'C': True}
    print(evaluate_boolean_expression(expr3, vars3))