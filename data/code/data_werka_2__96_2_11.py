import re
from typing import Dict, Any

def evaluate_boolean_expression(expression: str, variables: Dict[str, bool]) -> bool:
    cleaned = expression.replace(' ', '')
    if not cleaned:
        raise ValueError("Empty expression")
    
    tokens = tokenize(cleaned)
    if not tokens:
        raise ValueError("No tokens found")
    
    parser = Parser(tokens)
    result = parser.parse_expression()
    
    if parser.index < len(parser.tokens):
        raise ValueError("Unexpected tokens after expression")
    
    return result

def tokenize(expr: str) -> list:
    token_pattern = re.compile(r'\(|\)|and|or|not|[A-Za-z_][A-Za-z0-9_]*')
    tokens = []
    for match in token_pattern.finditer(expr):
        tokens.append(match.group())
    return tokens

class Parser:
    def __init__(self, tokens: list):
        self.tokens = tokens
        self.index = 0

    def parse_expression(self) -> bool:
        left = self.parse_or()
        while self.index < len(self.tokens) and self.tokens[self.index] == 'or':
            self.index += 1
            right = self.parse_or()
            left = left or right
        return left

    def parse_or(self) -> bool:
        left = self.parse_and()
        while self.index < len(self.tokens) and self.tokens[self.index] == 'and':
            self.index += 1
            right = self.parse_and()
            left = left and right
        return left

    def parse_and(self) -> bool:
        if self.index < len(self.tokens) and self.tokens[self.index] == 'not':
            self.index += 1
            operand = self.parse_and()
            return not operand
        
        return self.parse_primary()

    def parse_primary(self) -> bool:
        if self.index >= len(self.tokens):
            raise ValueError("Unexpected end of expression")
        
        token = self.tokens[self.index]
        
        if token == '(':
            self.index += 1
            result = self.parse_expression()
            if self.index >= len(self.tokens) or self.tokens[self.index] != ')':
                raise ValueError("Missing closing parenthesis")
            self.index += 1
            return result
        
        if token == ')':
            raise ValueError("Unexpected closing parenthesis")
        
        if token in ('and', 'or', 'not'):
            raise ValueError(f"Unexpected operator: {token}")
        
        if token.lower() == 'true':
            self.index += 1
            return True
        if token.lower() == 'false':
            self.index += 1
            return False
        
        if token.isidentifier():
            self.index += 1
            if token in variables:
                val = variables[token]
                if not isinstance(val, bool):
                    raise ValueError(f"Variable {token} is not a boolean")
                return val
            raise ValueError(f"Undefined variable: {token}")
        
        raise ValueError(f"Unknown token: {token}")

if __name__ == '__main__':
    variables = {'A': True, 'B': False, 'C': True}
    expr1 = '((A and B) or C)'
    result1 = evaluate_boolean_expression(expr1, variables)
    print(result1)
    
    expr2 = 'A and (B or C)'
    result2 = evaluate_boolean_expression(expr2, variables)
    print(result2)
    
    expr3 = 'not A'
    result3 = evaluate_boolean_expression(expr3, variables)
    print(result3)