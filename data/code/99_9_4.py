import operator
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
        self.operators = {
            'AND': operator.and_,
            'OR': operator.or_,
            '==': operator.eq,
            '!=': operator.ne,
            '>': operator.gt,
            '<': operator.lt,
            '>=': operator.ge,
            '<=': operator.le,
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
                op = ""
                start = i
                while i < len(expression) and expression[i].isalpha():
                    i += 1
                token = expression[start:i]
                if token in self.operators:
                    tokens.append(token)
                else:
                    tokens.append(token)
            elif char in '()':
                tokens.append(char)
            elif char in '+-*/=!<>':
                tokens.append(char)
            else:
                tokens.append(char)
            i += 1
        return tokens
    def _parse_and_evaluate(self, tokens):
        values = []
        ops = []
        for token in tokens:
            if token == '(':
                values.append(token)
            elif token == ')':
                balance = 0
                sub_expression = []
                while len(values) > 0 and values[-1] != '(':
                    sub_expression.append(values.pop())
                if not values or values[-1] != '(':
                    raise ValueError("Mismatched parentheses: Missing opening parenthesis.")
                values.pop()              
                while values and values[-1] != '(':
                    op = values.pop()
                    if op in self.operators:
                        right = values.pop()
                        values.append(self.operators[op](right, values[-1]))
                    else:
                        raise ValueError(f"Invalid expression structure inside parentheses: {op}")
                if values and values[-1] == '(':
                    pass
                else:
                    values.append(values.pop())
            elif token in self.operators:
                if token == 'NOT':
                    if len(values) < 1:
                        raise ValueError("NOT requires an operand.")
                    operand = values.pop()
                    values.append(not operand)
                    continue
                if len(values) < 2:
                    raise ValueError(f"Insufficient operands for binary operator: {token}")
                right = values.pop()
                left = values.pop()
                op_func = self.operators[token]
                values.append(op_func(left, right))
            else:
                try:
                    values.append(eval(token))
                except Exception:
                    values.append(token)
        if not values:
            return None
        return values[0]
    def evaluate(self, expression):
        tokens = self._tokenize(expression)
        if not tokens:
            return None
        try:
            result = self._parse_and_evaluate(tokens)
            return result
        except ValueError as e:
            raise ValueError(f"Expression Error: {e}")
        except Exception as e:
            raise ValueError(f"An unexpected error occurred during evaluation: {e}")
if __name__ == '__main__':
    analyzer = BooleanExpressionAnalyzer()
    test_cases = [
        ("NOT (A AND B)", "True"),
        ("(A AND B) OR C", "True"),
        ("A OR NOT B", "True"),
        ("A == B", "False"),
        ("5 > 3 AND 10 < 20", "True"),
        ("NOT (5 > 3)", "False"),
        ("(5 > 3) AND (10 < 20)", "True"),
        ("A == B OR C == D", "False"),
        ("NOT (A AND (B OR C))", "False"),
        ("A > 5 AND B < 10", "True"),
        ("NOT (A AND B)", "False"),
        ("NOT (5 > 3)", "False"),
        ("A == B", "False"),
        ("5 > 3", "True"),
        ("A AND B OR C", "True"),
        ("NOT A", "False"),
        ("NOT (A OR B)", "False"),
        ("A == B AND C == D", "False"),
        ("NOT (A AND B)", "False"),
        ("A > 5 AND B < 10", "True"),
        ("NOT (A AND (B OR C))", "False"),
    ]
    for expression, expected in test_cases:
        try:
            result = analyzer.evaluate(expression)
            assert result == expected, f"Expression: '{expression}', Expected: {expected}, Got: {result}"
            print(f"PASS: '{expression}' -> {result}")
        except ValueError as e:
            print(f"FAIL (Error): '{expression}' -> {e}")
        except AssertionError as e:
            print(f"FAIL (Assertion): {e}")
        print("-" * 20)
    print("All sample tests completed.")