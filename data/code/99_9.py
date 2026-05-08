import re
class BooleanExpressionAnalyzer:
    def __init__(self):
        self.precedence = {
            '(': 0,
            ')': 0,
            'NOT': 3,
            'AND': 2,
            'OR': 1
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
                    if expression[i:i+4].upper() == 'TRUE':
                        tokens.append('TRUE')
                        i += 4
                    elif expression[i:i+5].upper() == 'FALSE':
                        tokens.append('FALSE')
                        i += 5
                    else:
                        raise ValueError(f"Unknown token starting at index {i}: {expression[i:]}")
            elif char in '()':
                tokens.append(char)
                i += 1
            else:
                raise ValueError(f"Invalid character in expression: {char} at index {i}")
        return tokens
    def _shunting_yard(self, tokens):
        output_queue = []
        operator_stack = []
        for token in tokens:
            if token in ('TRUE', 'FALSE'):
                output_queue.append(token)
            elif token == '(':
                operator_stack.append(token)
            elif token == ')':
                while operator_stack and operator_stack[-1] != '(':
                    output_queue.append(operator_stack.pop())
                if not operator_stack or operator_stack[-1] != '(':
                    raise ValueError("Mismatched parentheses")
                operator_stack.pop()
            elif token in self.precedence:
                while (operator_stack and operator_stack[-1] != '(' and
                       self.precedence.get(operator_stack[-1], 0) >= self.precedence[token]):
                    output_queue.append(operator_stack.pop())
                operator_stack.append(token)
            else:
                raise ValueError(f"Unexpected token during Shunting-Yard: {token}")
        while operator_stack:
            top = operator_stack.pop()
            if top == '(':
                raise ValueError("Mismatched parentheses")
            output_queue.append(top)
        return output_queue
    def _evaluate(self, postfix_tokens, values):
        stack = []
        for token in postfix_tokens:
            if token == 'TRUE':
                stack.append(True)
            elif token == 'FALSE':
                stack.append(False)
            elif token in ('NOT'):
                if len(stack) < 1:
                    raise ValueError("Syntax error: NOT requires an operand")
                operand = stack.pop()
                stack.append(not operand)
            elif token in ('AND'):
                if len(stack) < 2:
                    raise ValueError("Syntax error: AND requires two operands")
                right = stack.pop()
                left = stack.pop()
                stack.append(left and right)
            elif token in ('OR'):
                if len(stack) < 2:
                    raise ValueError("Syntax error: OR requires two operands")
                right = stack.pop()
                left = stack.pop()
                stack.append(left or right)
            else:
                raise ValueError(f"Unknown token during evaluation: {token}")
        if len(stack) != 1:
            raise ValueError("Invalid expression structure remaining on stack")
        return stack[0]
    def analyze(self, expression):
        tokens = self._tokenize(expression)
        postfix = self._shunting_yard(tokens)
        result = self._evaluate(postfix, [])
        return result
if __name__ == '__main__':
    analyzer = BooleanExpressionAnalyzer()
    test_cases = [
        ("TRUE AND FALSE OR TRUE", True),
        ("(TRUE OR FALSE) AND TRUE", True),
        ("NOT TRUE", False),
        ("NOT (FALSE AND TRUE)", True),
        ("TRUE OR (FALSE AND NOT TRUE)", True),
        ("FALSE AND FALSE", False),
        ("(TRUE OR FALSE) AND (TRUE OR FALSE)", True),
        ("NOT (TRUE AND FALSE)", True),
        ("TRUE OR NOT FALSE", True),
        ("TRUE AND (FALSE OR TRUE)", True),
        ("NOT (TRUE AND FALSE OR TRUE)", False),
        ("TRUE AND TRUE AND FALSE", False)
    ]
    print("--- Boolean Expression Analysis ---")
    for expression, expected in test_cases:
        try:
            result = analyzer.analyze(expression)
            status = "PASS" if result == expected else f"FAIL (Expected: {expected}, Got: {result})"
            print(f"Expression: '{expression}'")
            print(f"Result: {result} | Status: {status}\n")
        except ValueError as e:
            print(f"Expression: '{expression}'")
            print(f"ERROR: {e}\n")
        except Exception as e:
            print(f"Expression: '{expression}'")
            print(f"UNEXPECTED ERROR: {e}\n")
    print("--- Additional Test Cases ---")
    try:
        result = analyzer.analyze("NOT (TRUE AND FALSE OR TRUE)")
        print(f"Expression: 'NOT (TRUE AND FALSE OR TRUE)'")
        print(f"Result: {result}")
    except Exception as e:
        print(f"Error on complex test: {e}")