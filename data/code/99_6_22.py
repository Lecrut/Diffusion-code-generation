from typing import List, Tuple, Union, Any
import re

class BooleanExpressionAnalyzer:
    def __init__(self, expression: str):
        self.original_expression = expression
        self.tokens = self._tokenize(expression)
        self.precedence_rules = {
            'NOT': 3,
            'AND': 2,
            'OR': 1
        }
        self.parsed_tree = self._parse()
        self.result = self._evaluate(self.parsed_tree)

    def _tokenize(self, expression: str) -> List[Tuple[str, Union[str, bool]]]:
        cleaned = expression.replace(' ', '')
        if not cleaned:
            raise ValueError("Empty expression")
        pattern = r'(\(|\)|AND|OR|NOT|True|False)'
        matches = re.findall(pattern, cleaned)
        if not matches:
            raise ValueError("No valid tokens found")
        tokens = []
        for match in matches:
            if match == 'True':
                tokens.append(('VALUE', True))
            elif match == 'False':
                tokens.append(('VALUE', False))
            else:
                tokens.append(('OP', match))
        return tokens

    def _parse(self) -> Any:
        if not self.tokens:
            raise ValueError("Empty expression")
        pos = [0]
        result = self._parse_or()
        if pos[0] != len(self.tokens):
            raise ValueError("Unexpected tokens at end")
        return result

    def _parse_or(self) -> Any:
        left = self._parse_and()
        while pos[0] < len(self.tokens) and self.tokens[pos[0]] == ('OP', 'OR'):
            pos[0] += 1
            right = self._parse_and()
            left = ('OR', left, right)
        return left

    def _parse_and(self) -> Any:
        left = self._parse_not()
        while pos[0] < len(self.tokens) and self.tokens[pos[0]] == ('OP', 'AND'):
            pos[0] += 1
            right = self._parse_not()
            left = ('AND', left, right)
        return left

    def _parse_not(self) -> Any:
        if pos[0] < len(self.tokens) and self.tokens[pos[0]] == ('OP', 'NOT'):
            pos[0] += 1
            operand = self._parse_not()
            return ('NOT', operand)
        return self._parse_primary()

    def _parse_primary(self) -> Any:
        if pos[0] >= len(self.tokens):
            raise ValueError("Unexpected end of expression")
        token = self.tokens[pos[0]]
        if token[0] == 'VALUE':
            pos[0] += 1
            return token
        elif token == ('OP', '('):
            pos[0] += 1
            expr = self._parse_or()
            if pos[0] >= len(self.tokens) or self.tokens[pos[0]] != ('OP', ')'):
                raise ValueError("Missing closing parenthesis")
            pos[0] += 1
            return expr
        else:
            raise ValueError(f"Unexpected token: {token}")

    def _evaluate(self, tree: Any) -> bool:
        if tree[0] == 'VALUE':
            return tree[1]
        elif tree[0] == 'NOT':
            return not self._evaluate(tree[1])
        elif tree[0] == 'AND':
            return self._evaluate(tree[1]) and self._evaluate(tree[2])
        elif tree[0] == 'OR':
            return self._evaluate(tree[1]) or self._evaluate(tree[2])
        else:
            raise ValueError(f"Unknown operator: {tree[0]}")

if __name__ == '__main__':
    analyzer = BooleanExpressionAnalyzer("True AND False OR True")
    print(analyzer.result)
    analyzer2 = BooleanExpressionAnalyzer("(True OR False) AND NOT False")
    print(analyzer2.result)