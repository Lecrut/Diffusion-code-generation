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
            if char.isalpha() or char == '(':
                if char == 'N' and expression[i:i+3].upper() == 'NOT':
                    tokens.append('NOT')
                    i += 3
                elif char == 'A' and expression[i:i+3].upper() == 'AND':
                    tokens.append('AND')
                    i += 3
                elif char == 'O' and expression[i:i+2].upper() == 'OR':
                    tokens.append('OR')
                    i += 2
                elif char == '(':
                    tokens.append('(')
                    i += 1
                else:
                    tokens.append(char)
                    i += 1
            elif char in '()':
                tokens.append(char)
                i += 1
            elif char in '=!><':
                op = char
                if i + 1 < len(expression) and expression[i+1] == '=':
                    op += '='
                    i += 2
                else:
                    i += 1
                tokens.append(op)
            else:
                raise ValueError(f"Invalid character encountered: {char}")
        return tokens
    def _apply_operator(self, op, values):
        if op == 'NOT':
            if len(values) < 1:
                raise ValueError("NOT requires one operand.")
            return not values[0]
        elif op in self.operators:
            if len(values) < 2:
                raise ValueError(f"{op} requires two operands.")
            op_func = self.operators[op]
            return op_func(values[0], values[1])
        else:
            raise ValueError(f"Unknown operator: {op}")
    def _evaluate_tokens(self, tokens):
        values = []
        ops = []
        for token in tokens:
            if token in self.precedence:
                if token == '(':
                    values.append(token)
                elif token == ')':
                    while ops and ops[-1] != '(':
                        op = ops.pop()
                        values.append(self._apply_operator(op, values))
                    if not ops or ops[-1] != '(':
                        raise ValueError("Mismatched parentheses.")
                    ops.pop()              
                else:
                    if token == 'NOT':
                        if len(values) < 1:
                            raise ValueError("NOT requires an operand.")
                        operand = values.pop()
                        values.append(self._apply_operator('NOT', [operand]))
                    else:
                        prec = self.precedence.get(token, 0)
                        while (ops and ops[-1] != '(' and 
                                self.precedence.get(ops[-1], -1) >= prec):
                            op = ops.pop()
                            values.append(self._apply_operator(op, values))
                        ops.append(token)
            else:
                try:
                    if token not in ('(', ')', 'NOT', 'AND', 'OR'):
                        values.append(eval(token))
                    else:
                        values.append(token)
                except Exception:
                    raise ValueError(f"Invalid operand encountered: {token}")
        while ops:
            op = ops.pop()
            if op == '(':
                raise ValueError("Mismatched parentheses remaining.")
            values.append(self._apply_operator(op, values))
        if len(values) != 1:
            raise ValueError("Invalid expression structure or too many operands left.")
        return values[0]
    def evaluate(self, expression):
        tokens = self._tokenize(expression)
        return self._evaluate_tokens(tokens)
if __name__ == '__main__':
    analyzer = BooleanExpressionAnalyzer()
    test_cases = [
        ("NOT (A AND B)", True),
        ("(A OR B) AND C", True),
        ("A AND (B OR C)", True),
        ("NOT A", False),
        ("A == B", False),
        ("5 > 3", True),
        ("10 <= 10", True),
        ("(5 > 3) AND (10 < 20)", True),
        ("NOT (A == B)", True),
        ("A AND NOT B", False),
        ("NOT (A OR B)", False),
        ("A == B OR A != B", True),
        ("A > 5 AND B < 10", True),
        ("(A AND B) OR (C AND D)", True),
        ("NOT (A AND (B OR C))", False),
        ("A > 10 OR NOT B", True),
        ("A == 5 AND B != 5", False),
        ("NOT (A AND B AND C)", False),
        ("A > 1 AND B < 2", True),
    ]
    print("--- Boolean Expression Analyzer Test Results ---")
    all_passed = True
    for expression, expected in test_cases:
        try:
            result = analyzer.evaluate(expression)
            status = "PASS" if result == expected else f"FAIL (Expected: {expected}, Got: {result})"
            print(f"Expression: '{expression}'")
            print(f"Result: {result} | Expected: {expected} | Status: {status}\n")
            if result != expected:
                all_passed = False
        except ValueError as e:
            print(f"Expression: '{expression}'")
            print(f"ERROR: {e}\n")
            all_passed = False
        except Exception as e:
            print(f"Expression: '{expression}'")
            print(f"UNEXPECTED ERROR: {e}\n")
            all_passed = False
    if all_passed:
        print("All hardcoded tests passed successfully.")
    else:
        print("Some tests failed.")