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
        pattern = r'\b(AND|OR|NOT|TRUE|FALSE)\b|[\(\)]'
        matches = re.findall(pattern, cleaned)
        if not matches:
            raise ValueError("No valid tokens found")
        if len(matches) % 2 == 0 and not re.match(r'^\((.*)\)$', cleaned):
            raise ValueError("Invalid token sequence length or structure")
        tokens = []
        for match in matches:
            if match in ('TRUE', 'FALSE'):
                tokens.append(('VALUE', match == 'TRUE'))
            elif match in ('AND', 'OR', 'NOT'):
                tokens.append(('OP', match))
            else:
                tokens.append(('PAREN', match))
        return tokens

    def _parse(self) -> Any:
        if not self.tokens:
            raise ValueError("No tokens to parse")
        pos = [0]
        result = self._parse_or()
        if pos[0] != len(self.tokens):
            raise ValueError("Unexpected tokens after expression")
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
        if token[0] == 'PAREN' and token[1] == '(':
            pos[0] += 1
            expr = self._parse_or()
            if pos[0] >= len(self.tokens) or self.tokens[pos[0]] != ('PAREN', ')'):
                raise ValueError("Missing closing parenthesis")
            pos[0] += 1
            return expr
        raise ValueError(f"Unexpected token: {token}")

    def _evaluate(self, node: Any) -> bool:
        if node[0] == 'VALUE':
            return node[1]
        if node[0] == 'NOT':
            return not self._evaluate(node[1])
        if node[0] == 'AND':
            return self._evaluate(node[1]) and self._evaluate(node[2])
        if node[0] == 'OR':
            return self._evaluate(node[1]) or self._evaluate(node[2])
        raise ValueError(f"Unknown node type: {node[0]}")

if __name__ == '__main__':
    analyzer = BooleanExpressionAnalyzer("TRUE AND NOT FALSE OR FALSE")
    print(analyzer.result)
    analyzer2 = BooleanExpressionAnalyzer("(TRUE OR FALSE) AND NOT (FALSE AND TRUE)")
    print(analyzer2.result)