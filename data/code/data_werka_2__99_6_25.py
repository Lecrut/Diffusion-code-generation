import re
from typing import List, Tuple, Union

class BooleanAnalyzer:
    def __init__(self, expr: str) -> None:
        self.expr = expr
        self.tokens = self._tokenize(expr)
        self.parsed = self._parse()
        self.result = self._evaluate(self.parsed)

    def _tokenize(self, expr: str) -> List[Tuple[str, Union[str, bool]]]:
        cleaned = expr.strip()
        if not cleaned:
            raise ValueError("Empty expression")
        pattern = r'\s*(NOT|AND|OR|XOR|TRUE|FALSE)\s*|[\(\)]'
        matches = re.finditer(pattern, cleaned)
        tokens = []
        for match in matches:
            word = match.group(1)
            if word:
                if word == 'TRUE':
                    tokens.append(('VAL', True))
                elif word == 'FALSE':
                    tokens.append(('VAL', False))
                else:
                    tokens.append(('OP', word))
            else:
                tokens.append(('PAREN', match.group(0)))
        if not tokens:
            raise ValueError("No valid tokens found")
        return tokens

    def _parse(self) -> List[Union[str, bool]]:
        precedence = {'NOT': 3, 'AND': 2, 'XOR': 1, 'OR': 0}
        ops = []
        output = []
        for token_type, token_val in self.tokens:
            if token_type == 'VAL':
                output.append(token_val)
            elif token_type == 'OP':
                while ops and ops[-1] != '(' and precedence.get(ops[-1], 0) >= precedence.get(token_val, 0):
                    output.append(ops.pop())
                ops.append(token_val)
            elif token_val == '(':
                ops.append(token_val)
            elif token_val == ')':
                while ops and ops[-1] != '(':
                    output.append(ops.pop())
                if not ops:
                    raise ValueError("Mismatched parentheses")
                ops.pop()
        while ops:
            top = ops.pop()
            if top == '(':
                raise ValueError("Mismatched parentheses")
            output.append(top)
        if len(output) == 1 and isinstance(output[0], bool):
            return output[0]
        return output

    def _evaluate(self, node: Union[str, bool, List[Union[str, bool]]]) -> bool:
        if isinstance(node, bool):
            return node
        stack = []
        for item in node:
            if isinstance(item, bool):
                stack.append(item)
            else:
                if item == 'NOT':
                    val = stack.pop()
                    stack.append(not val)
                elif item in ('AND', 'OR', 'XOR'):
                    right = stack.pop()
                    left = stack.pop()
                    if item == 'AND':
                        stack.append(left and right)
                    elif item == 'OR':
                        stack.append(left or right)
                    elif item == 'XOR':
                        stack.append(left ^ right)
        return stack[0]

if __name__ == '__main__':
    analyzer = BooleanAnalyzer("TRUE AND FALSE")
    print(f"Result: {analyzer.result}")
    
    analyzer2 = BooleanAnalyzer("(TRUE OR FALSE) AND NOT FALSE")
    print(f"Result: {analyzer2.result}")