import re
class BooleanExpressionAnalyzer:
    def __init__(self):
        self.precedence = {
            '(': 0,
            ')': 0,
            'NOT': 3,
            'AND': 2,
            'OR': 1,
            '==': 4,
            '!=': 4,
            '>': 5,
            '<': 5,
            '>=': 6,
            '<=': 6,
        }
    def _tokenize(self, expression):
        tokens = []
        i = 0
        while i < len(expression):
            char = expression[i]
            if char.isspace():
                i += 1
                continue
            if char.isalpha():
                if char.upper() == 'NOT':
                    tokens.append('NOT')
                    i += 3
                elif char.upper() == 'AND':
                    tokens.append('AND')
                    i += 3
                elif char.upper() == 'OR':
                    tokens.append('OR')
                    i += 2
                else:
                    tokens.append(char)
                    i += 1
            elif char in '()':
                tokens.append(char)
                i += 1
            elif re.match(r'[0-9\.\+\-\!\(\)\=\<\>\!\+\-\*]', char):
                if char == '=':
                    if i + 1 < len(expression) and expression[i+1] in '><!':
                        op = expression[i:i+2]
                        if op in ('==', '!='):
                            tokens.append(op)
                            i += 2
                            continue
                        elif op in ('>=', '<='):
                            tokens.append(op)
                            i += 2
                            continue
                tokens.append(char)
                i += 1
            else:
                tokens.append(char)
                i += 1
        return tokens
    def _shunting_yard(self, tokens):
        output_queue = []
        operator_stack = []
        for token in tokens:
            if token in ('NOT', 'AND', 'OR', '(', ')'):
                if token == '(':
                    operator_stack.append(token)
                elif token == ')':
                    while operator_stack and operator_stack[-1] != '(':
                        output_queue.append(operator_stack.pop())
                    if not operator_stack or operator_stack[-1] != '(':
                        raise ValueError("Mismatched parentheses")
                    operator_stack.pop()
                else:
                    if token in self.precedence:
                        while (operator_stack and operator_stack[-1] != '(' and
                               self.precedence.get(operator_stack[-1], -1) >= self.precedence.get(token, -1)):
                            output_queue.append(operator_stack.pop())
                        operator_stack.append(token)
            else:
                output_queue.append(token)
        while operator_stack:
            if operator_stack[-1] == '(':
                raise ValueError("Mismatched parentheses")
            output_queue.append(operator_stack.pop())
        return output_queue
    def _evaluate(self, postfix_tokens, values):
        stack = []
        for token in postfix_tokens:
            if token in ('NOT'):
                if len(stack) < 1:
                    raise ValueError("Insufficient operands for NOT")
                operand = stack.pop()
                result = not operand
                stack.append(result)
            elif token in ('AND', 'OR'):
                if len(stack) < 2:
                    raise ValueError(f"Insufficient operands for {token}")
                right = stack.pop()
                left = stack.pop()
                if token == 'AND':
                    result = left and right
                elif token == 'OR':
                    result = left or right
                stack.append(result)
            else:
                try:
                    value = float(token)
                    stack.append(value)
                except ValueError:
                    raise ValueError(f"Invalid token encountered during evaluation: {token}")
        if len(stack) != 1:
            raise ValueError("Invalid expression structure or too many operands remaining")
        return stack[0]
    def analyze(self, expression):
        tokens = self._tokenize(expression)
        postfix = self._shunting_yard(tokens)
        result = self._evaluate(postfix, [])
        return result
if __name__ == '__main__':
    analyzer = BooleanExpressionAnalyzer()
    test_cases = [
        ("NOT (5 > 3 AND 10 == 10)", False),
        ("(5 > 3) AND (10 == 10)", True),
        ("NOT (5 > 3)", False),
        ("5 > 3 OR 10 < 5", True),
        ("NOT (5 > 3 AND 10 != 10)", True),
        ("(10 >= 5) AND (2 < 10)", True),
        ("5 > 3 AND 10 > 12", False),
        ("NOT (5 > 3 AND 10 > 12)", True),
        ("NOT (5 > 3 OR 10 < 5)", False),
        ("(5 > 3) AND (10 == 10) OR (2 < 10)", True),
        ("NOT (5 > 3 AND 10 == 10)", False),
        ("5 > 3", False),
        ("10 == 10", True),
        ("NOT 5", "Error"),
        ("(5 > 3", "Error"),
        ("5 > 3 AND", "Error"),
        ("5 > 3 AND 10", "Error"),
    ]
    for expression, expected in test_cases:
        try:
            result = analyzer.analyze(expression)
            status = "PASS" if result == expected else f"FAIL (Expected: {expected}, Got: {result})"
            print(f"Expression: '{expression}'")
            print(f"Result: {result} | Status: {status}\n")
        except ValueError as e:
            print(f"Expression: '{expression}'")
            print(f"Error: {e}\n")
        except Exception as e:
            print(f"Expression: '{expression}'")
            print(f"Unexpected Error: {e}\n")