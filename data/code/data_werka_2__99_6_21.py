import re
from typing import List, Tuple, Union

class BooleanExpressionAnalyzer:
    def __init__(self, expression: str):
        self.original_expression = expression
        self.tokens = self._tokenize(expression)
        self.precedence_rules = {
            'NOT': 3,
            'AND': 2,
            'OR': 1
        }
        self.result = self._evaluate()

    def _tokenize(self, expression: str) -> List[Tuple[str, Union[str, bool]]]:
        cleaned = expression.replace(' ', '')
        if not cleaned:
            raise ValueError("Empty expression")
        
        pattern = r'\b(AND|OR|NOT)\b|True|False|\(|\)'
        matches = re.finditer(pattern, cleaned)
        
        tokens = []
        last_end = 0
        for match in matches:
            if match.start() > last_end:
                raise ValueError(f"Unexpected characters at index {match.start()}")
            word = match.group(0)
            if word in ('AND', 'OR', 'NOT'):
                tokens.append(('OP', word))
            elif word == 'True':
                tokens.append(('VAL', True))
            elif word == 'False':
                tokens.append(('VAL', False))
            elif word == '(':
                tokens.append(('LPAREN', '('))
            elif word == ')':
                tokens.append(('RPAREN', ')'))
            last_end = match.end()
        
        if last_end < len(cleaned):
            raise ValueError(f"Unexpected characters at index {last_end}")
        
        if not tokens:
            raise ValueError("No valid tokens found")
            
        return tokens

    def _evaluate(self) -> bool:
        if not self.tokens:
            raise ValueError("Empty expression")
        
        result, _ = self._parse_or(0)
        return result

    def _parse_or(self, pos: int) -> Tuple[bool, int]:
        left, pos = self._parse_and(pos)
        
        while pos < len(self.tokens) and self.tokens[pos][0] == 'OP' and self.tokens[pos][1] == 'OR':
            pos += 1
            right, pos = self._parse_and(pos)
            left = left or right
        
        return left, pos

    def _parse_and(self, pos: int) -> Tuple[bool, int]:
        left, pos = self._parse_not(pos)
        
        while pos < len(self.tokens) and self.tokens[pos][0] == 'OP' and self.tokens[pos][1] == 'AND':
            pos += 1
            right, pos = self._parse_not(pos)
            left = left and right
        
        return left, pos

    def _parse_not(self, pos: int) -> Tuple[bool, int]:
        if pos < len(self.tokens) and self.tokens[pos][0] == 'OP' and self.tokens[pos][1] == 'NOT':
            pos += 1
            val, pos = self._parse_not(pos)
            return not val, pos
        
        return self._parse_primary(pos)

    def _parse_primary(self, pos: int) -> Tuple[bool, int]:
        if pos >= len(self.tokens):
            raise ValueError("Unexpected end of expression")
        
        token_type, token_val = self.tokens[pos]
        
        if token_type == 'VAL':
            return token_val, pos + 1
        
        if token_type == 'LPAREN':
            pos += 1
            val, pos = self._parse_or(pos)
            if pos >= len(self.tokens) or self.tokens[pos][0] != 'RPAREN':
                raise ValueError("Missing closing parenthesis")
            return val, pos + 1
        
        raise ValueError(f"Unexpected token: {token_val}")

    def get_result(self) -> bool:
        return self.result

    def get_precedence_rules(self) -> dict:
        return self.precedence_rules

def analyze_boolean_expression(expression: str) -> dict:
    analyzer = BooleanExpressionAnalyzer(expression)
    return {
        'expression': expression,
        'result': analyzer.get_result(),
        'precedence': analyzer.get_precedence_rules()
    }

if __name__ == '__main__':
    expr = "True AND (False OR NOT False)"
    output = analyze_boolean_expression(expr)
    print(output)