from typing import List, Tuple, Union, Any
import re

class BooleanExpressionAnalyzer:

    def __init__(self, expression: str):
        self.original_expression = expression
        self.tokens = self._tokenize(expression)
        self.precedence_rules = [['NOT'], ['AND'], ['OR'], ['XOR']]
        self.operator_map = {'AND': lambda a, b: a and b, 'OR': lambda a, b: a or b, 'XOR': lambda a, b: a ^ b, 'NOT': lambda a: not a}

    def _tokenize(self, expression: str) -> List[Tuple[str, Union[str, bool]]]:
        cleaned = expression.replace(' ', '')
        if not cleaned:
            raise ValueError('Empty expression')
        pattern = '\\b(AND|OR|NOT|TRUE|FALSE)\\b|[\\(\\)]'
        matches = re.findall(pattern, cleaned)
        tokens = []
        for match in matches:
            if match in ('TRUE', 'FALSE'):
                tokens.append(('VALUE', match == 'TRUE'))
            elif match in ('AND', 'OR', 'NOT', 'XOR'):
                tokens.append(('OPERATOR', match))
            else:
                tokens.append(('PAREN', match))
        if not tokens:
            raise ValueError('No valid tokens found')
        return tokens

    def _parse(self) -> List[Any]:
        precedence = {'NOT': 3, 'AND': 2, 'OR': 1, 'XOR': 1}
        output_queue = []
        operator_stack = []
        for token_type, token_value in self.tokens:
            if token_type == 'VALUE':
                output_queue.append(('VALUE', token_value))
            elif token_type == 'OPERATOR':
                while operator_stack and operator_stack[-1] != '(' and (precedence.get(operator_stack[-1], 0) >= precedence.get(token_value, 0)):
                    output_queue.append(('OPERATOR', operator_stack.pop()))
                operator_stack.append(token_value)
            elif token_type == 'PAREN':
                if token_value == '(':
                    operator_stack.append('(')
                elif token_value == ')':
                    while operator_stack and operator_stack[-1] != '(':
                        output_queue.append(('OPERATOR', operator_stack.pop()))
                    if not operator_stack:
                        raise ValueError('Mismatched parentheses')
                    operator_stack.pop()
        while operator_stack:
            op = operator_stack.pop()
            if op == '(':
                raise ValueError('Mismatched parentheses')
            output_queue.append(('OPERATOR', op))
        return output_queue

    def _evaluate_node(self, parsed: List[Any]) -> bool:
        if not parsed:
            raise ValueError('Empty parsed expression')
        stack = []
        for item in parsed:
            if item[0] == 'VALUE':
                stack.append(item[1])
            elif item[0] == 'OPERATOR':
                op = item[1]
                if op == 'NOT':
                    if len(stack) < 1:
                        raise ValueError('Insufficient operands for NOT')
                    a = stack.pop()
                    stack.append(not a)
                else:
                    if len(stack) < 2:
                        raise ValueError('Insufficient operands for binary operator')
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(self.operator_map[op](a, b))
        if len(stack) != 1:
            raise ValueError('Invalid expression result')
        return stack[0]

    def evaluate(self) -> bool:
        parsed = self._parse()
        return self._evaluate_node(parsed)
if __name__ == '__main__':
    test_cases = [('TRUE AND FALSE', False), ('TRUE OR FALSE', True), ('NOT TRUE', False), ('(TRUE OR FALSE) AND TRUE', True), ('TRUE XOR FALSE', True), ('NOT (TRUE AND FALSE)', True), ('TRUE AND (FALSE OR TRUE)', True), ('(TRUE XOR TRUE) AND TRUE', False)]
    for expr, expected in test_cases:
        analyzer = BooleanExpressionAnalyzer(expr)
        result = analyzer.evaluate()
        status = 'PASS' if result == expected else 'FAIL'
        print(f'{status}: {expr} = {result} (expected {expected})')