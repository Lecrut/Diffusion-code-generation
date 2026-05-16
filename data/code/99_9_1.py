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
                    tokens.append(char)
                    i += 1
            elif char in '()':
                tokens.append(char)
                i += 1
            else:
                if expression[i:i+4] == 'True':
                    tokens.append('True')
                    i += 4
                elif expression[i:i+5] == 'False':
                    tokens.append('False')
                    i += 5
                else:
                    raise ValueError(f"Invalid character in expression: {char}")
        return tokens
    def _apply_operator(self, values, operator):
        if operator == 'NOT':
            if len(values) < 1:
                raise ValueError("Syntax Error: NOT requires an operand.")
            operand = values.pop()
            values.append(not operand)
        elif operator in ('AND', 'OR'):
            if len(values) < 2:
                raise ValueError(f"Syntax Error: {operator} requires two operands.")
            right = values.pop()
            left = values.pop()
            if operator == 'AND':
                values.append(left and right)
            elif operator == 'OR':
                values.append(left or right)
        else:
            raise ValueError(f"Unknown operator: {operator}")
    def _evaluate_tokens(self, tokens):
        values = []
        for token in tokens:
            if token == '(':
                values.append(token)
            elif token == ')':
                while values and values[-1] != '(':
                    op = values.pop()
                    self._apply_operator(values, op)
                if not values or values[-1] != '(':
                    raise ValueError("Mismatched parentheses: Missing opening parenthesis.")
                values.pop()              
            elif token in ('True', 'False'):
                values.append(token == 'True')
            elif token == 'NOT':
                self._apply_operator(values, 'NOT')
            elif token in ('AND', 'OR'):
                self._apply_operator(values, token)
            else:
                raise ValueError(f"Unrecognized token during evaluation: {token}")
        return values
    def analyze(self, expression):
        if not expression:
            return False
        tokens = self._tokenize(expression)
        if not tokens:
            return False
        try:
            result = self._evaluate_tokens(tokens)
            return result
        except ValueError as e:
            raise ValueError(f"Expression Analysis Error: {e}")
        except Exception as e:
            raise ValueError(f"An unexpected error occurred during analysis: {e}")
if __name__ == '__main__':
    analyzer = BooleanExpressionAnalyzer()
    test_cases = [
        ("True AND False", False),
        ("(True OR False) AND True", True),
        ("NOT True", False),
        ("NOT (True AND False)", True),
        ("True OR (False AND True)", True),
        ("NOT (True OR False)", False),
        ("True", True),
        ("(True OR False)", True),
        ("NOT (NOT True)", True),
        ("True AND True AND True", True),
        ("False OR False", False),
        ("NOT True AND False", False),
        ("True OR NOT False", True),
        ("NOT (True AND False OR True)", False),
        ("NOT (True OR False)", False),
        ("(True AND False) OR True", True),
    ]
    print("--- Running Test Cases ---")
    for expression, expected in test_cases:
        try:
            result = analyzer.analyze(expression)
            assert result == expected, f"Expression: '{expression}', Expected: {expected}, Got: {result}"
            print(f"PASS: '{expression}' -> {result}")
        except ValueError as e:
            print(f"FAIL (Error): '{expression}' -> {e}")
        except AssertionError as e:
            print(f"FAIL (Assertion): {e}")
    print("\n--- Additional Complex Test ---")
    try:
        complex_expr = "NOT (True AND (False OR NOT False))"
        result = analyzer.analyze(complex_expr)
        print(f"Expression: '{complex_expr}'")
        print(f"Result: {result}")
    except ValueError as e:
        print(f"Error on complex test: {e}")