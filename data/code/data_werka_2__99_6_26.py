import re
from typing import List, Tuple, Union, Any

class BooleanEvaluator:

    def __init__(self, expression: str):
        self.expression = expression
        self.tokens = self._tokenize(expression)
        self.precedence = {'OR': 1, 'AND': 2, 'NOT': 3}
        self.ops = {'OR': lambda a, b: a or b, 'AND': lambda a, b: a and b, 'NOT': lambda a: not a}

    def _tokenize(self, expr: str) -> List[Tuple[str, Any]]:
        cleaned = expr.replace(' ', '')
        if not cleaned:
            raise ValueError('Empty expression')
        pattern = '\\b(AND|OR|NOT|TRUE|FALSE)\\b|[\\(\\)]'
        matches = re.finditer(pattern, cleaned)
        result = []
        for match in matches:
            token = match.group(0)
            if token in ('TRUE', 'FALSE'):
                result.append(('VAL', token == 'TRUE'))
            elif token in ('AND', 'OR', 'NOT'):
                result.append(('OP', token))
            elif token == '(':
                result.append(('LPAREN', '('))
            elif token == ')':
                result.append(('RPAREN', ')'))
            else:
                raise ValueError(f'Unknown token: {token}')
        if not result:
            raise ValueError('No valid tokens found')
        return result

    def evaluate(self) -> bool:
        if not self.tokens:
            raise ValueError('Empty expression')
        parsed = self._parse()
        return self._eval_node(parsed)

    def _parse(self) -> List[Any]:
        precedence = self.precedence
        ops = self.ops
        tokens = self.tokens
        output = []
        stack = []
        i = 0
        while i < len(tokens):
            token_type, token_val = tokens[i]
            if token_type == 'VAL':
                output.append(token_val)
            elif token_type == 'LPAREN':
                stack.append(token_val)
            elif token_type == 'RPAREN':
                while stack and stack[-1] != '(':
                    op = stack.pop()
                    output.append(op)
                if not stack:
                    raise ValueError('Mismatched parentheses')
                stack.pop()
            elif token_type == 'OP':
                while stack and stack[-1] != '(' and (precedence.get(stack[-1], 0) >= precedence.get(token_val, 0)):
                    output.append(stack.pop())
                stack.append(token_val)
            i += 1
        while stack:
            op = stack.pop()
            if op == '(':
                raise ValueError('Mismatched parentheses')
            output.append(op)
        return output

    def _eval_node(self, node: Any) -> bool:
        if isinstance(node, bool):
            return node
        op = node
        if op == 'NOT':
            if len(self.tokens) < 2:
                raise ValueError('NOT requires one operand')
            val = self.tokens[0][1] if self.tokens[0][0] == 'VAL' else self._eval_node(self.tokens[0])
            return not val
        raise ValueError('Complex expression evaluation not fully implemented in this simplified version')

    def get_tokens(self) -> List[Tuple[str, Any]]:
        return self.tokens
if __name__ == '__main__':
    test_cases = [('TRUE AND FALSE', False), ('TRUE OR FALSE', True), ('NOT TRUE', False), ('(TRUE OR FALSE) AND TRUE', True), ('TRUE AND (FALSE OR TRUE)', True)]
    for expr, expected in test_cases:
        evaluator = BooleanEvaluator(expr)
        try:
            result = evaluator.evaluate()
            status = 'PASS' if result == expected else 'FAIL'
            print(f'{status}: {expr} -> {result} (expected {expected})')
        except Exception as e:
            print(f'ERROR: {expr} -> {e}')