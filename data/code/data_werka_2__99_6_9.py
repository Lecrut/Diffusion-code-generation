from typing import List, Tuple, Union
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
        self.parentheses_map = {
            '(': 'right_paren',
            ')': 'right_paren'
        }

    def _tokenize(self, expression: str) -> List[Tuple[str, Union[str, None]]]:
        pattern = r'\s*(NOT|AND|OR|XOR|AND_NOT|OR_NOT|XOR_NOT|NOT_AND|NOT_OR|NOT_XOR|\(|\)|True|False)\s*'
        matches = re.finditer(pattern, expression)
        tokens = []
        last_end = 0
        for match in matches:
            tokens.append((match.group(1), match.start()))
            last_end = match.end()
        if last_end < len(expression):
            remaining = expression[last_end:]
            if remaining.strip():
                raise ValueError(f"Unexpected characters in expression: {remaining}")
        return tokens

    def _convert_to_postfix(self) -> List[str]:
        output_queue = []
        operator_stack = []
        precedence = {'NOT': 3, 'AND': 2, 'OR': 1, 'XOR': 0}
        
        for token, _ in self.tokens:
            if token in ('True', 'False'):
                output_queue.append(token)
            elif token == '(':
                operator_stack.append('(')
            elif token == ')':
                while operator_stack and operator_stack[-1] != '(':
                    output_queue.append(operator_stack.pop())
                if not operator_stack:
                    raise ValueError("Mismatched parentheses")
                operator_stack.pop()
            elif token in precedence:
                while (operator_stack and 
                       operator_stack[-1] != '(' and
                       precedence.get(operator_stack[-1], 0) >= precedence[token]):
                    output_queue.append(operator_stack.pop())
                operator_stack.append(token)
        
        while operator_stack:
            op = operator_stack.pop()
            if op == '(':
                raise ValueError("Mismatched parentheses")
            output_queue.append(op)
            
        return output_queue

    def _evaluate_postfix(self, postfix: List[str]) -> bool:
        stack = []
        for token in postfix:
            if token == 'True':
                stack.append(True)
            elif token == 'False':
                stack.append(False)
            elif token == 'NOT':
                if len(stack) < 1:
                    raise ValueError("Invalid expression: missing operand for NOT")
                operand = stack.pop()
                stack.append(not operand)
            elif token in ('AND', 'OR', 'XOR'):
                if len(stack) < 2:
                    raise ValueError(f"Invalid expression: missing operand for {token}")
                right = stack.pop()
                left = stack.pop()
                result = self.operator_map[token](left, right)
                stack.append(result)
            else:
                raise ValueError(f"Unknown token: {token}")
        
        if len(stack) != 1:
            raise ValueError("Invalid expression: too many operands")
        return stack[0]

    def analyze(self) -> dict:
        try:
            postfix = self._convert_to_postfix()
            result = self._evaluate_postfix(postfix)
            return {
                'expression': self.original_expression,
                'postfix_notation': ' '.join(postfix),
                'result': result,
                'precedence_rules': self.precedence_rules
            }
        except ValueError as e:
            return {
                'expression': self.original_expression,
                'error': str(e),
                'result': None
            }

def evaluate_expression(expression: str) -> dict:
    analyzer = BooleanExpressionAnalyzer(expression)
    return analyzer.analyze()

if __name__ == '__main__':
    expr1 = "True AND False OR True"
    result1 = evaluate_expression(expr1)
    print(result1)
    
    expr2 = "(True OR False) AND NOT False"
    result2 = evaluate_expression(expr2)
    print(result2)