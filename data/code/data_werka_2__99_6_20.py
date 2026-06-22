from typing import List, Tuple, Union, Any
import re

class BooleanEvaluator:
    def __init__(self, expression: str):
        self.expression = expression
        self.tokens = self._tokenize(expression)
        self.precedence = {'NOT': 3, 'AND': 2, 'OR': 1}
        self.ast = self._parse()

    def _tokenize(self, expr: str) -> List[Tuple[str, Union[str, bool]]]:
        cleaned = expr.replace(' ', '').upper()
        if not cleaned:
            raise ValueError("Empty expression")
        pattern = r'\b(AND|OR|NOT|TRUE|FALSE)\b|[\(\)]'
        matches = re.findall(pattern, cleaned)
        if ''.join(matches) != cleaned:
            raise ValueError("Invalid characters in expression")
        tokens = []
        for m in matches:
            if m == 'TRUE':
                tokens.append(('LITERAL', True))
            elif m == 'FALSE':
                tokens.append(('LITERAL', False))
            elif m in ('AND', 'OR', 'NOT'):
                tokens.append(('OP', m))
            else:
                tokens.append(('BRACKET', m))
        return tokens

    def _parse(self) -> Any:
        pos = 0
        def parse_or() -> Any:
            nonlocal pos
            left = parse_and()
            while pos < len(self.tokens) and self.tokens[pos][0] == 'OP' and self.tokens[pos][1] == 'OR':
                pos += 1
                right = parse_and()
                left = ('OR', left, right)
            return left
        def parse_and() -> Any:
            nonlocal pos
            left = parse_not()
            while pos < len(self.tokens) and self.tokens[pos][0] == 'OP' and self.tokens[pos][1] == 'AND':
                pos += 1
                right = parse_not()
                left = ('AND', left, right)
            return left
        def parse_not() -> Any:
            nonlocal pos
            if pos < len(self.tokens) and self.tokens[pos][0] == 'OP' and self.tokens[pos][1] == 'NOT':
                pos += 1
                operand = parse_not()
                return ('NOT', operand)
            return parse_primary()
        def parse_primary() -> Any:
            nonlocal pos
            if pos >= len(self.tokens):
                raise ValueError("Unexpected end of expression")
            token = self.tokens[pos]
            if token[0] == 'LITERAL':
                pos += 1
                return ('LITERAL', token[1])
            if token[0] == 'BRACKET' and token[1] == '(':
                pos += 1
                expr = parse_or()
                if pos >= len(self.tokens) or self.tokens[pos][1] != ')':
                    raise ValueError("Missing closing parenthesis")
                pos += 1
                return expr
            raise ValueError(f"Unexpected token: {token}")
        ast = parse_or()
        if pos < len(self.tokens):
            raise ValueError("Unexpected tokens at end of expression")
        return ast

    def evaluate(self) -> bool:
        return self._eval_node(self.ast)

    def _eval_node(self, node: Any) -> bool:
        if node[0] == 'LITERAL':
            return node[1]
        if node[0] == 'NOT':
            return not self._eval_node(node[1])
        if node[0] == 'AND':
            return self._eval_node(node[1]) and self._eval_node(node[2])
        if node[0] == 'OR':
            return self._eval_node(node[1]) or self._eval_node(node[2])
        raise ValueError(f"Unknown node type: {node[0]}")

if __name__ == '__main__':
    test_cases = [
        ("TRUE AND FALSE", False),
        ("TRUE OR FALSE", True),
        ("NOT TRUE", False),
        ("(TRUE OR FALSE) AND FALSE", False),
        ("NOT (TRUE AND FALSE)", True),
        ("TRUE AND (FALSE OR TRUE)", True),
    ]
    for expr, expected in test_cases:
        evaluator = BooleanEvaluator(expr)
        result = evaluator.evaluate()
        print(f"{expr} = {result} (Expected: {expected}) {'PASS' if result == expected else 'FAIL'}")
        assert result == expected, f"Failed for {expr}"
    print("All tests passed.")