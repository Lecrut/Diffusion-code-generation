from typing import List, Tuple, Any, Optional
import re

class BooleanExpressionParser:
    def __init__(self, expression: str):
        self.expression = expression.strip()
        self.tokens: List[Tuple[str, Any]] = self._tokenize(self.expression)
        self.pos = 0
        self.precedence_map = {'OR': 1, 'AND': 2, 'XOR': 3, 'NOT': 4}

    def _tokenize(self, expr: str) -> List[Tuple[str, Any]]:
        if not expr:
            raise ValueError("Empty expression")
        pattern = re.compile(r'\s+|\b(AND|OR|XOR|NOT|TRUE|FALSE)\b|\(|\)|\^')
        tokens = []
        for match in pattern.finditer(expr):
            word = match.group(0)
            if word.isspace():
                continue
            if word == 'TRUE':
                tokens.append(('BOOL', True))
            elif word == 'FALSE':
                tokens.append(('BOOL', False))
            elif word in ('AND', 'OR', 'XOR', 'NOT'):
                tokens.append(('OP', word))
            elif word == '(':
                tokens.append(('LPAREN', '('))
            elif word == ')':
                tokens.append(('RPAREN', ')'))
            elif word == '^':
                tokens.append(('OP', 'XOR'))
            else:
                raise ValueError(f"Unexpected token: {word}")
        if not tokens:
            raise ValueError("No valid tokens found")
        return tokens

    def parse(self) -> bool:
        if not self.tokens:
            raise ValueError("Empty expression")
        result = self._parse_or()
        if self.pos < len(self.tokens):
            raise ValueError("Unexpected token after expression")
        return result

    def _parse_or(self) -> bool:
        left = self._parse_and()
        while self.pos < len(self.tokens) and self.tokens[self.pos][0] == 'OP' and self.tokens[self.pos][1] == 'OR':
            self.pos += 1
            right = self._parse_and()
            left = left or right
        return left

    def _parse_and(self) -> bool:
        left = self._parse_xor()
        while self.pos < len(self.tokens) and self.tokens[self.pos][0] == 'OP' and self.tokens[self.pos][1] == 'AND':
            self.pos += 1
            right = self._parse_xor()
            left = left and right
        return left

    def _parse_xor(self) -> bool:
        left = self._parse_not()
        while self.pos < len(self.tokens) and self.tokens[self.pos][0] == 'OP' and self.tokens[self.pos][1] == 'XOR':
            self.pos += 1
            right = self._parse_not()
            left = left ^ right
        return left

    def _parse_not(self) -> bool:
        if self.pos < len(self.tokens) and self.tokens[self.pos][0] == 'OP' and self.tokens[self.pos][1] == 'NOT':
            self.pos += 1
            operand = self._parse_not()
            return not operand
        return self._parse_primary()

    def _parse_primary(self) -> bool:
        if self.pos >= len(self.tokens):
            raise ValueError("Unexpected end of expression")
        token_type, token_value = self.tokens[self.pos]
        if token_type == 'BOOL':
            self.pos += 1
            return token_value
        elif token_type == 'LPAREN':
            self.pos += 1
            result = self._parse_or()
            if self.pos >= len(self.tokens) or self.tokens[self.pos][0] != 'RPAREN':
                raise ValueError("Missing closing parenthesis")
            self.pos += 1
            return result
        else:
            raise ValueError(f"Unexpected token: {token_value}")

if __name__ == '__main__':
    test_cases = [
        ("TRUE AND FALSE", False),
        ("TRUE OR FALSE", True),
        ("NOT TRUE", False),
        ("TRUE XOR TRUE", False),
        ("(TRUE OR FALSE) AND TRUE", True),
        ("NOT (TRUE AND FALSE)", True),
        ("TRUE AND TRUE OR FALSE", True),
    ]
    for expr, expected in test_cases:
        analyzer = BooleanExpressionParser(expr)
        result = analyzer.parse()
        print(f"{expr} = {result} (Expected: {expected})")
        assert result == expected, f"Failed for {expr}"