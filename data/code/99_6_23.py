from typing import List, Tuple, Union, Any
import re

class BooleanExpressionAnalyzer:
    def __init__(self, expression: str):
        self.original_expression = expression
        self.tokens = self._tokenize(expression)
        self.precedence_rules = {
            'NOT': 3,
            'AND': 2,
            'OR': 1,
            'LPAREN': 0,
            'RPAREN': 0
        }
        self.parsed_tree = self._parse()
        self.result = self._evaluate(self.parsed_tree)

    def _tokenize(self, expression: str) -> List[Tuple[str, Union[str, bool]]]:
        cleaned = expression.replace(' ', '')
        if not cleaned:
            raise ValueError("Empty expression")
        pattern = r'\b(AND|OR|NOT|TRUE|FALSE)\b|[\(\)]'
        matches = re.finditer(pattern, cleaned)
        tokens = []
        for match in matches:
            word = match.group(0)
            if word in ('TRUE', 'FALSE'):
                tokens.append(('VAL', word == 'TRUE'))
            elif word in ('AND', 'OR', 'NOT'):
                tokens.append(('OP', word))
            elif word == '(':
                tokens.append(('LPAREN', None))
            elif word == ')':
                tokens.append(('RPAREN', None))
            else:
                raise ValueError(f"Unknown token: {word}")
        if len(tokens) == 0:
            raise ValueError("No valid tokens found")
        return tokens

    def _parse(self) -> Any:
        pos = 0
        def parse_expr():
            nonlocal pos
            left = parse_term()
            while pos < len(self.tokens) and self.tokens[pos][0] == 'OP' and self.tokens[pos][1] == 'OR':
                pos += 1
                right = parse_term()
                left = ('OR', left, right)
            return left

        def parse_term():
            nonlocal pos
            left = parse_factor()
            while pos < len(self.tokens) and self.tokens[pos][0] == 'OP' and self.tokens[pos][1] == 'AND':
                pos += 1
                right = parse_factor()
                left = ('AND', left, right)
            return left

        def parse_factor():
            nonlocal pos
            if pos < len(self.tokens) and self.tokens[pos][0] == 'OP' and self.tokens[pos][1] == 'NOT':
                pos += 1
                operand = parse_factor()
                return ('NOT', operand)
            return parse_primary()

        def parse_primary():
            nonlocal pos
            if pos >= len(self.tokens):
                raise ValueError("Unexpected end of expression")
            token_type, token_val = self.tokens[pos]
            if token_type == 'VAL':
                pos += 1
                return ('VAL', token_val)
            elif token_type == 'LPAREN':
                pos += 1
                expr = parse_expr()
                if pos >= len(self.tokens) or self.tokens[pos][0] != 'RPAREN':
                    raise ValueError("Missing closing parenthesis")
                pos += 1
                return expr
            else:
                raise ValueError(f"Unexpected token: {token_type}")

        result = parse_expr()
        return result

    def _evaluate(self, node: Any) -> bool:
        if node is None:
            return False
        node_type = node[0]
        if node_type == 'VAL':
            return node[1]
        elif node_type == 'AND':
            return self._evaluate(node[1]) and self._evaluate(node[2])
        elif node_type == 'OR':
            return self._evaluate(node[1]) or self._evaluate(node[2])
        elif node_type == 'NOT':
            return not self._evaluate(node[1])
        else:
            raise ValueError(f"Unknown node type: {node_type}")

    def get_result(self) -> bool:
        return self.result

if __name__ == '__main__':
    expr1 = "TRUE AND FALSE"
    analyzer1 = BooleanExpressionAnalyzer(expr1)
    print(f"{expr1} = {analyzer1.get_result()}")

    expr2 = "TRUE OR FALSE"
    analyzer2 = BooleanExpressionAnalyzer(expr2)
    print(f"{expr2} = {analyzer2.get_result()}")

    expr3 = "NOT TRUE"
    analyzer3 = BooleanExpressionAnalyzer(expr3)