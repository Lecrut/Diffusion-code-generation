import re
from typing import List, Tuple, Union, Any

class BooleanEvaluator:
    def __init__(self, expression: str):
        self.expression = expression
        self.precedence = {'NOT': 3, 'AND': 2, 'OR': 1}
        self.tokens = self._tokenize(expression)
        self.ast = self._parse()
        self.result = self._evaluate(self.ast)

    def _tokenize(self, expr: str) -> List[Tuple[str, Any]]:
        cleaned = expr.replace(' ', '')
        if not cleaned:
            raise ValueError("Empty expression")
        pattern = r'\b(AND|OR|NOT|TRUE|FALSE)\b|[\(\)]'
        matches = re.findall(pattern, cleaned)
        if not matches:
            raise ValueError("No valid tokens found")
        tokens = []
        for m in matches:
            if m == 'TRUE':
                tokens.append(('VAL', True))
            elif m == 'FALSE':
                tokens.append(('VAL', False))
            else:
                tokens.append(('OP', m))
        return tokens

    def _parse(self) -> List[Any]:
        prec = self.precedence
        def parse_expr(idx: int) -> Tuple[Any, int]:
            left, idx = parse_term(idx)
            while idx < len(self.tokens) and self.tokens[idx][0] == 'OP' and self.tokens[idx][1] in ('OR',):
                op = self.tokens[idx][1]
                idx += 1
                right, idx = parse_term(idx)
                left = (op, left, right)
            return left, idx

        def parse_term(idx: int) -> Tuple[Any, int]:
            left, idx = parse_factor(idx)
            while idx < len(self.tokens) and self.tokens[idx][0] == 'OP' and self.tokens[idx][1] in ('AND',):
                op = self.tokens[idx][1]
                idx += 1
                right, idx = parse_factor(idx)
                left = (op, left, right)
            return left, idx

        def parse_factor(idx: int) -> Tuple[Any, int]:
            if idx >= len(self.tokens):
                raise ValueError("Unexpected end of expression")
            token = self.tokens[idx]
            if token[0] == 'VAL':
                return token[1], idx + 1
            if token[0] == 'OP' and token[1] == '(':
                val, idx = parse_expr(idx + 1)
                if idx < len(self.tokens) and self.tokens[idx][0] == 'OP' and self.tokens[idx][1] == ')':
                    return val, idx + 1
                raise ValueError("Mismatched parentheses")
            if token[0] == 'OP' and token[1] == 'NOT':
                operand, idx = parse_factor(idx + 1)
                return ('NOT', operand), idx
            if token[0] == 'OP' and token[1] == 'XOR':
                raise ValueError("XOR not supported in this simplified parser")
            raise ValueError(f"Unexpected token: {token}")

        root, end_idx = parse_expr(0)
        if end_idx != len(self.tokens):
            raise ValueError("Extra tokens after expression")
        return root

    def _evaluate(self, node: Any) -> bool:
        if isinstance(node, bool):
            return node
        op, left, right = node
        if op == 'AND':
            return self._evaluate(left) and self._evaluate(right)
        elif op == 'OR':
            return self._evaluate(left) or self._evaluate(right)
        elif op == 'NOT':
            return not self._evaluate(left)
        return False

if __name__ == '__main__':
    tests = [
        ("TRUE AND FALSE", False),
        ("TRUE OR FALSE", True),
        ("NOT FALSE", True),
        ("TRUE AND TRUE", True),
        ("FALSE OR FALSE", False),
    ]
    for expr, expected in tests:
        evaluator = BooleanEvaluator(expr)
        actual = evaluator.result
        assert actual == expected, f"Failed for {expr}: expected {expected}, got {actual}"
        print(f"{expr} = {actual}")
    print("All tests passed.")