from typing import List, Tuple, Union
import re

class BooleanExpressionEvaluator:
    def __init__(self, expression: str):
        self.expression = expression
        self.tokens = self._tokenize(expression)
        self.precedence = {'NOT': 3, 'AND': 2, 'OR': 1}
        self.tree = self._parse()

    def _tokenize(self, expr: str) -> List[Tuple[str, Union[str, bool]]]:
        cleaned = expr.replace(' ', '')
        if not cleaned:
            raise ValueError("Empty expression")
        tokens = []
        i = 0
        while i < len(cleaned):
            char = cleaned[i]
            if char == '(':
                tokens.append(('LPAREN', '('))
                i += 1
            elif char == ')':
                tokens.append(('RPAREN', ')'))
                i += 1
            elif char == '!':
                tokens.append(('NOT', 'NOT'))
                i += 1
            elif char == '&':
                tokens.append(('AND', 'AND'))
                i += 1
            elif char == '|':
                tokens.append(('OR', 'OR'))
                i += 1
            elif char == '^':
                tokens.append(('XOR', 'XOR'))
                i += 1
            elif char == 'T' and cleaned[i:i+4] == 'TRUE':
                tokens.append(('BOOL', True))
                i += 4
            elif char == 'F' and cleaned[i:i+5] == 'FALSE':
                tokens.append(('BOOL', False))
                i += 5
            elif char == 't' and cleaned[i:i+4] == 'true':
                tokens.append(('BOOL', True))
                i += 4
            elif char == 'f' and cleaned[i:i+5] == 'false':
                tokens.append(('BOOL', False))
                i += 5
            else:
                raise ValueError(f"Unexpected character: {char}")
        return tokens

    def _parse(self) -> any:
        pos = 0
        def parse_expr():
            nonlocal pos
            left = parse_term()
            while pos < len(self.tokens) and self.tokens[pos][0] == 'OR':
                op = self.tokens[pos][1]
                pos += 1
                right = parse_term()
                left = ('OR', left, right)
            return left

        def parse_term():
            nonlocal pos
            left = parse_factor()
            while pos < len(self.tokens) and self.tokens[pos][0] == 'AND':
                op = self.tokens[pos][1]
                pos += 1
                right = parse_factor()
                left = ('AND', left, right)
            return left

        def parse_factor():
            nonlocal pos
            if pos >= len(self.tokens):
                raise ValueError("Unexpected end of expression")
            token_type, token_val = self.tokens[pos]
            if token_type == 'LPAREN':
                pos += 1
                expr = parse_expr()
                if pos < len(self.tokens) and self.tokens[pos][0] == 'RPAREN':
                    pos += 1
                else:
                    raise ValueError("Missing closing parenthesis")
                return expr
            elif token_type == 'NOT':
                pos += 1
                operand = parse_factor()
                return ('NOT', operand)
            elif token_type == 'BOOL':
                pos += 1
                return ('BOOL', token_val)
            else:
                raise ValueError(f"Unexpected token: {token_val}")

        return parse_expr()

    def evaluate(self) -> bool:
        return self._eval_node(self.tree)

    def _eval_node(self, node: any) -> bool:
        if node[0] == 'BOOL':
            return node[1]
        elif node[0] == 'NOT':
            return not self._eval_node(node[1])
        elif node[0] == 'AND':
            return self._eval_node(node[1]) and self._eval_node(node[2])
        elif node[0] == 'OR':
            return self._eval_node(node[1]) or self._eval_node(node[2])
        else:
            raise ValueError(f"Unknown node type: {node[0]}")

if __name__ == '__main__':
    evaluator = BooleanExpressionEvaluator("TRUE AND FALSE")
    result = evaluator.evaluate()
    print(result)
    
    evaluator2 = BooleanExpressionEvaluator("TRUE OR FALSE")
    result2 = evaluator2.evaluate()
    print(result2)