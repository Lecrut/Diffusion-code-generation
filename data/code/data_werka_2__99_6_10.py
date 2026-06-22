from typing import List, Tuple, Union

class BooleanExpressionAnalyzer:
    def __init__(self, expression: str):
        self.original_expression = expression
        self.tokens = self._tokenize(expression)
        self.precedence_rules = [
            ['NOT'],
            ['AND'],
            ['OR'],
            ['XOR']
        ]
        self.operator_map = {
            'AND': lambda a, b: a and b,
            'OR': lambda a, b: a or b,
            'XOR': lambda a, b: a ^ b,
            'NOT': lambda a: not a
        }

    def _tokenize(self, expression: str) -> List[str]:
        cleaned = expression.replace('(', ' ( ').replace(')', ' ) ')
        words = cleaned.split()
        tokens = []
        for word in words:
            upper = word.upper()
            if upper in ('AND', 'OR', 'XOR', 'NOT', '(', ')'):
                tokens.append(upper)
            elif upper in ('TRUE', 'FALSE'):
                tokens.append(upper)
            else:
                raise ValueError(f"Unknown token: {word}")
        return tokens

    def evaluate(self) -> bool:
        parsed = self._parse_expression(0, len(self.tokens))
        return parsed[0]

    def _parse_expression(self, start: int, end: int) -> Tuple[bool, int]:
        left, current = self._parse_or(start, end)
        while current < end and self.tokens[current] == 'OR':
            current += 1
            right, next_pos = self._parse_or(current, end)
            left = left or right
            current = next_pos
        return left, current

    def _parse_or(self, start: int, end: int) -> Tuple[bool, int]:
        left, current = self._parse_and(start, end)
        while current < end and self.tokens[current] == 'OR':
            current += 1
            right, next_pos = self._parse_and(current, end)
            left = left or right
            current = next_pos
        return left, current

    def _parse_and(self, start: int, end: int) -> Tuple[bool, int]:
        left, current = self._parse_xor(start, end)
        while current < end and self.tokens[current] == 'AND':
            current += 1
            right, next_pos = self._parse_xor(current, end)
            left = left and right
            current = next_pos
        return left, current

    def _parse_xor(self, start: int, end: int) -> Tuple[bool, int]:
        left, current = self._parse_not(start, end)
        while current < end and self.tokens[current] == 'XOR':
            current += 1
            right, next_pos = self._parse_not(current, end)
            left = left ^ right
            current = next_pos
        return left, current

    def _parse_not(self, start: int, end: int) -> Tuple[bool, int]:
        if start < end and self.tokens[start] == 'NOT':
            operand, next_pos = self._parse_not(start + 1, end)
            return not operand, next_pos
        return self._parse_primary(start, end)

    def _parse_primary(self, start: int, end: int) -> Tuple[bool, int]:
        if start >= end:
            raise ValueError("Unexpected end of expression")
        token = self.tokens[start]
        if token == '(':
            value, next_pos = self._parse_expression(start + 1, end)
            if next_pos >= end or self.tokens[next_pos] != ')':
                raise ValueError("Missing closing parenthesis")
            return value, next_pos + 1
        elif token == 'TRUE':
            return True, start + 1
        elif token == 'FALSE':
            return False, start + 1
        else:
            raise ValueError(f"Unexpected token: {token}")

if __name__ == '__main__':
    analyzer = BooleanExpressionAnalyzer("TRUE AND NOT FALSE OR FALSE")
    result = analyzer.evaluate()
    print(result)