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
        self.associativity = {
            'AND': 'left',
            'OR': 'left',
            '==': 'left',
            '!=': 'left',
            '>': 'left',
            '<': 'left',
            '>=': 'left',
            '<=': 'left',
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
                elif char == '=' and i + 1 < len(expression) and expression[i+1] == '=':
                    tokens.append('==')
                    i += 2
                elif char == '!' and i + 1 < len(expression) and expression[i+1] == '=':
                    tokens.append('!=')
                    i += 2
                elif char == '>' and i + 1 < len(expression) and expression[i+1] == '=':
                    tokens.append('>=')
                    i += 2
                elif char == '<' and i + 1 < len(expression) and expression[i+1] == '=':
                    tokens.append('<=')
                    i += 2
                elif char == '(':
                    tokens.append('(')
                    i += 1
                elif char == ')':
                    tokens.append(')')
                    i += 1
                else:
                    tokens.append(char)
                    i += 1
            else:
                tokens.append(char)
                i += 1
        return tokens
    def _parse_to_rpn(self, tokens):
        output = []
        op_stack = []
        for token in tokens:
            if token in self.operators:
                op_stack.append(token)
            elif token == '(':
                op_stack.append(token)
            elif token == ')':
                while op_stack and op_stack[-1] != '(':
                    output.append(op_stack.pop())
                if op_stack and op_stack[-1] == '(':
                    op_stack.pop()
                else:
                    raise ValueError("Mismatched parentheses")
            else:
                output.append(token)
        while op_stack:
            if op_stack[-1] == '(':
                raise ValueError("Mismatched parentheses")
            output.append(op_stack.pop())
        return output
    def _apply_operator(self, op, values):
        if op == 'NOT':
            if len(values) < 1:
                raise ValueError("NOT requires one operand")
            result = not values[0]
            values.pop(0)
            values.insert(0, result)
            return
        if op in ('==', '!=', '>', '<', '>=', '<='):
            if len(values) < 2:
                raise ValueError(f"{op} requires two operands")
            right = values.pop(0)
            left = values.pop(0)
            func = self.operators[op]
            values.insert(0, func(left, right))
            return
        if op in ('AND', 'OR'):
            if len(values) < 2:
                raise ValueError(f"{op} requires two operands")
            right = values.pop(0)
            left = values.pop(0)
            func = self.operators[op]
            values.insert(0, func(left, right))
            return
    def evaluate(self, expression):
        tokens = self._tokenize(expression)
        rpn_tokens = self._parse_to_rpn(tokens)
        if not rpn_tokens:
            return None
        stack = []
        for token in rpn_tokens:
            if token in self.operators:
                if token == 'NOT':
                    self._apply_operator(token, stack)
                else:
                    self._apply_operator(token, stack)
            else:
                stack.append(token)
        if len(stack) != 1:
            raise ValueError("Invalid expression structure")
        return stack[0]
if __name__ == '__main__':
    analyzer = BooleanExpressionAnalyzer()
    test_cases = [
        ("NOT (A AND B)", True),
        ("(A AND B) OR C", True),
        ("A OR B AND C", True),
        ("A == B", False),
        ("10 > 5 AND 2 < 8", True),
        ("NOT (A > 5)", False),
        ("A == B OR A != B", True),
        ("A > 5 AND B < 10", True),
        ("(A OR B) AND (C OR D)", True),
        ("NOT (A AND (B OR C))", False),
        ("A == 10 AND B == 2", False),
        ("A > 5 OR B < 10", True),
        ("A > 5 AND B > 10", False),
        ("A == 5 AND B == 5", True),
        ("NOT (A AND B AND C)", False),
        ("A > 5 AND NOT B", False),
    ]
    for expression, expected in test_cases:
        try:
            result = analyzer.evaluate(expression)
            assert result == expected, f"Expression: '{expression}', Expected: {expected}, Got: {result}"
            print(f"PASS: '{expression}' -> {result}")
        except Exception as e:
            print(f"FAIL (Error): '{expression}' raised {e}")
    print("\n--- Additional Complex Test ---")
    complex_expr = "((A == 1) OR B) AND (C != D)"
    try:
        result = analyzer.evaluate(complex_expr)
        print(f"Expression: '{complex_expr}' -> {result}")
    except Exception as e:
        print(f"FAIL (Error): '{complex_expr}' raised {e}")