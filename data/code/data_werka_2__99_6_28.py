import re
from typing import List, Union, Tuple

class BooleanAnalyzer:

    def __init__(self, expr: str) -> None:
        self.expr = expr
        self.tokens = []
        self.precedence = {'NOT': 3, 'AND': 2, 'OR': 1}
        self._tokenize()
        self.ast = self._parse()
        self.result = self._evaluate(self.ast)

    def _tokenize(self) -> None:
        pattern = '\\b(TRUE|FALSE|NOT|AND|OR|XOR)\\b|\\(|\\)'
        raw = re.findall(pattern, self.expr)
        self.tokens = [(t, 'OP' if t in ('NOT', 'AND', 'OR', 'XOR') else 'VAL' if t in ('TRUE', 'FALSE') else 'LPAREN' if t == '(' else 'RPAREN') for t in raw]
        if not self.tokens:
            raise ValueError('Invalid expression')

    def _parse(self) -> any:
        pos = [0]
        return self._or_expr(pos)

    def _or_expr(self, pos: list) -> any:
        left = self._xor_expr(pos)
        while pos[0] < len(self.tokens) and self.tokens[pos[0]][0] == 'OR':
            pos[0] += 1
            right = self._xor_expr(pos)
            left = ('OR', left, right)
        return left

    def _xor_expr(self, pos: list) -> any:
        left = self._and_expr(pos)
        while pos[0] < len(self.tokens) and self.tokens[pos[0]][0] == 'XOR':
            pos[0] += 1
            right = self._and_expr(pos)
            left = ('XOR', left, right)
        return left

    def _and_expr(self, pos: list) -> any:
        left = self._not_expr(pos)
        while pos[0] < len(self.tokens) and self.tokens[pos[0]][0] == 'AND':
            pos[0] += 1
            right = self._not_expr(pos)
            left = ('AND', left, right)
        return left

    def _not_expr(self, pos: list) -> any:
        if pos[0] < len(self.tokens) and self.tokens[pos[0]][0] == 'NOT':
            pos[0] += 1
            operand = self._not_expr(pos)
            return ('NOT', operand)
        return self._primary(pos)

    def _primary(self, pos: list) -> any:
        if pos[0] >= len(self.tokens):
            raise ValueError('Unexpected end of expression')
        token_type = self.tokens[pos[0]][1]
        if token_type == 'VAL':
            val = self.tokens[pos[0]][0] == 'TRUE'
            pos[0] += 1
            return ('VAL', val)
        if token_type == 'LPAREN':
            pos[0] += 1
            expr = self._or_expr(pos)
            if pos[0] >= len(self.tokens) or self.tokens[pos[0]][0] != ')':
                raise ValueError('Missing closing parenthesis')
            pos[0] += 1
            return expr
        raise ValueError(f'Unexpected token: {self.tokens[pos[0]]}')

    def _evaluate(self, node: any) -> bool:
        if node[0] == 'VAL':
            return node[1]
        if node[0] == 'NOT':
            return not self._evaluate(node[1])
        if node[0] == 'AND':
            return self._evaluate(node[1]) and self._evaluate(node[2])
        if node[0] == 'OR':
            return self._evaluate(node[1]) or self._evaluate(node[2])
        if node[0] == 'XOR':
            return self._evaluate(node[1]) ^ self._evaluate(node[2])
        raise ValueError('Unknown node type')

    def get_result(self) -> bool:
        return self.result

    def get_ast(self) -> any:
        return self.ast
if __name__ == '__main__':
    analyzer = BooleanAnalyzer('TRUE AND (FALSE OR NOT TRUE)')
    print(f'Result: {analyzer.get_result()}')
    print(f'AST: {analyzer.get_ast()}')