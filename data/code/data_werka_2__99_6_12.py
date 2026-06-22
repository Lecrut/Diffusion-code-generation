from typing import List, Tuple, Union, Any
import re

class BooleanExpressionAnalyzer:
    def __init__(self, expression: str):
        self.original_expression = expression
        self.tokens = self._tokenize(expression)
        self.precedence_rules = [
            ['NOT'],
            ['AND'],
            ['OR'],
            ['XOR']
        ]
        self.operator_map = {
            'AND': lambda a, b: a and b,
            'OR': lambda a, b: a or b,
            'XOR': lambda a, b: a ^ b,
            'NOT': lambda a: not a
        }

    def _tokenize(self, expression: str) -> List[str]:
        cleaned = expression.replace(' ', '')
        if not cleaned:
            raise ValueError("Empty expression")
        pattern = r'\b(AND|OR|NOT|TRUE|FALSE)\b|[\(\)]'
        matches = re.findall(pattern, cleaned)
        if not matches:
            raise ValueError("No valid tokens found")
        result = []
        for match in matches:
            if match in ('TRUE', 'FALSE'):
                result.append(match)
            else:
                result.append(match)
        return result

    def _parse(self) -> List[Any]:
        precedence = {
            'NOT': 3,
            'AND': 2,
            'OR': 1,
            'XOR': 0
        }
        output_queue = []
        operator_stack = []
        i = 0
        while i < len(self.tokens):
            token = self.tokens[i]
            if token in ('TRUE', 'FALSE'):
                output_queue.append(token)
            elif token == '(':
                operator_stack.append(token)
            elif token == ')':
                while operator_stack and operator_stack[-1] != '(':
                    output_queue.append(operator_stack.pop())
                if not operator_stack:
                    raise ValueError("Mismatched parentheses")
                operator_stack.pop()
            else:
                while (operator_stack and operator_stack[-1] != '(' and
                       precedence.get(operator_stack[-1], 0) >= precedence.get(token, 0)):
                    output_queue.append(operator_stack.pop())
                operator_stack.append(token)
            i += 1
        while operator_stack:
            top = operator_stack.pop()
            if top == '(':
                raise ValueError("Mismatched parentheses")
            output_queue.append(top)
        return output_queue

    def _evaluate(self, postfix: List[Any]) -> bool:
        stack = []
        for token in postfix:
            if token == 'TRUE':
                stack.append(True)
            elif token == 'FALSE':
                stack.append(False)
            elif token == 'NOT':
                if len(stack) < 1:
                    raise ValueError("Insufficient operands for NOT")
                operand = stack.pop()
                stack.append(not operand)
            elif token in ('AND', 'OR', 'XOR'):
                if len(stack) < 2:
                    raise ValueError("Insufficient operands for binary operator")
                right = stack.pop()
                left = stack.pop()
                result = self.operator_map[token](left, right)
                stack.append(result)
        if len(stack) != 1:
            raise ValueError("Invalid expression structure")
        return stack[0]

    def analyze(self) -> dict:
        postfix = self._parse()
        result = self._evaluate(postfix)
        return {
            'expression': self.original_expression,
            'tokens': self.tokens,
            'postfix': postfix,
            'result': result
        }

if __name__ == '__main__':
    expr = "TRUE AND FALSE"
    analyzer = BooleanExpressionAnalyzer(expr)
    analysis = analyzer.analyze()
    print(analysis)