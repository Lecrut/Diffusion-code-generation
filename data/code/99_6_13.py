from typing import List, Tuple, Union
import re

class BooleanExpressionEvaluator:
    def __init__(self, expression: str):
        self.expression = expression
        self.tokens = self._tokenize(expression)
        self.precedence = {'NOT': 3, 'AND': 2, 'OR': 1, 'XOR': 1}
        self.result = self._evaluate()

    def _tokenize(self, expr: str) -> List[Tuple[str, Union[str, bool]]]:
        cleaned = re.sub(r'\s+', '', expr)
        if not cleaned:
            raise ValueError("Empty expression")
        pattern = r'\b(AND|OR|NOT|XOR|TRUE|FALSE)\b|[\(\)]|[^ ]'
        matches = re.findall(pattern, cleaned)
        if not matches:
            raise ValueError("No valid tokens found")
        tokens = []
        for match in matches:
            if match in ('TRUE', 'FALSE'):
                tokens.append(('VAL', match == 'TRUE'))
            elif match in ('AND', 'OR', 'NOT', 'XOR'):
                tokens.append(('OP', match))
            elif match in ('(', ')'):
                tokens.append(('PAREN', match))
            else:
                raise ValueError(f"Unexpected token: {match}")
        return tokens

    def _evaluate(self) -> bool:
        if not self.tokens:
            raise ValueError("Empty token stream")
        pos = 0
        result, pos = self._parse_or(self.tokens, pos)
        if pos < len(self.tokens):
            raise ValueError(f"Unexpected token at end: {self.tokens[pos]}")
        return result

    def _parse_or(self, tokens: List[Tuple[str, Union[str, bool]]], pos: int) -> Tuple[bool, int]:
        left, pos = self._parse_xor(tokens, pos)
        while pos < len(tokens) and tokens[pos][0] == 'OP' and tokens[pos][1] == 'OR':
            pos += 1
            right, pos = self._parse_xor(tokens, pos)
            left = left or right
        return left, pos

    def _parse_xor(self, tokens: List[Tuple[str, Union[str, bool]]], pos: int) -> Tuple[bool, int]:
        left, pos = self._parse_and(tokens, pos)
        while pos < len(tokens) and tokens[pos][0] == 'OP' and tokens[pos][1] == 'XOR':
            pos += 1
            right, pos = self._parse_and(tokens, pos)
            left = left ^ right
        return left, pos

    def _parse_and(self, tokens: List[Tuple[str, Union[str, bool]]], pos: int) -> Tuple[bool, int]:
        left, pos = self._parse_not(tokens, pos)
        while pos < len(tokens) and tokens[pos][0] == 'OP' and tokens[pos][1] == 'AND':
            pos += 1
            right, pos = self._parse_not(tokens, pos)
            left = left and right
        return left, pos

    def _parse_not(self, tokens: List[Tuple[str, Union[str, bool]]], pos: int) -> Tuple[bool, int]:
        if pos < len(tokens) and tokens[pos][0] == 'OP' and tokens[pos][1] == 'NOT':
            pos += 1
            val, pos = self._parse_not(tokens, pos)
            return not val, pos
        return self._parse_primary(tokens, pos)

    def _parse_primary(self, tokens: List[Tuple[str, Union[str, bool]]], pos: int) -> Tuple[bool, int]:
        if pos >= len(tokens):
            raise ValueError("Unexpected end of expression")
        token_type, token_val = tokens[pos]
        if token_type == 'VAL':
            return token_val, pos + 1
        elif token_type == 'PAREN' and token_val == '(':
            pos += 1
            val, pos = self._parse_or(tokens, pos)
            if pos >= len(tokens) or tokens[pos][1] != ')':
                raise ValueError("Missing closing parenthesis")
            return val, pos + 1
        else:
            raise ValueError(f"Unexpected token: {tokens[pos]}")

    def get_result(self) -> bool:
        return self.result

if __name__ == '__main__':
    expr1 = "TRUE AND FALSE OR TRUE"
    evaluator1 = BooleanExpressionEvaluator(expr1)