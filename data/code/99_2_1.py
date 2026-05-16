class OperatorPrecedence:
    def parse_expression(self, expression):
        tokens = []
        current_token = ""
        i = 0
        while i < len(expression):
            char = expression[i]
            if char.isspace():
                i += 1
                continue
            if char.isalnum() or char in "+-*/&|^!<>=":
                current_token += char
            else:
                if current_token:
                    tokens.append(current_token)
                current_token = ""
            i += 1
        if current_token:
            tokens.append(current_token)
        return tokens
    def get_precedence(self, operator):
        if operator in ('+', '-'):
            return 2
        if operator in ('*', '/', '%'):
            return 3
        if operator in ('<<', '>>', '>>>'):
            return 4
        if operator in ('&'):
            return 5
        if operator in ('|'):
            return 5
        if operator in ('^'):
            return 6
        if operator in ('==', '!='):
            return 7
        if operator in ('<=', '>='):
            return 8
        if operator in ('<', '>'):
            return 9
        return 10
    def evaluate_expression(self, expression):
        tokens = self.parse_expression(expression)
        if not tokens:
            return None
        values = []
        operators = []
        for token in tokens:
            if token.isdigit() or (token.startswith('-') and token[1:].isdigit()):
                values.append(float(token))
            elif token in ('+', '-', '*', '/', '%', '&', '|', '^', '<<', '>>', '>>>', '==', '!=', '<', '>', '<=', '>='):
                operators.append(token)
            else:
                pass
        if not values:
            return None
        if not operators:
            return values
        def apply_op(op, b, a):
            if op == '+': return a + b
            if op == '-': return a - b
            if op == '*': return a * b
            if op == '/':
                if b == 0: raise ZeroDivisionError
                return a / b
            if op == '%': return a % b
            if op == '&': return a & b
            if op == '|': return a | b
            if op == '^': return a ** b
            if op == '<<': return a << b
            if op == '>>': return a >> b
            if op == '>>>': return a >> b
            if op == '==': return a == b
            if op == '!=': return a != b
            if op == '<': return a < b
            if op == '>': return a > b
            if op == '<=': return a <= b
            if op == '>=': return a >= b
            return None
        result = values[0]
        op_index = 0
        output_values = []
        output_ops = []
        op_stack = []
        def process_operation():
            op = op_stack.pop()
            if len(output_values) < 2:
                raise ValueError("Insufficient operands")
            b = output_values.pop()
            a = output_values.pop()
            result = apply_op(op, b, a)
            output_values.append(result)
        for token in tokens:
            if token.isdigit() or (token.startswith('-') and token[1:].isdigit()):
                output_values.append(float(token))
            elif token in ('+', '-', '*', '/', '%', '&', '|', '^', '<<', '>>', '>>>', '==', '!=', '<', '>', '<=', '>='):
                prec1 = self.get_precedence(token)
                while (op_stack and op_stack[-1] != '(' and 
                       self.get_precedence(op_stack[-1]) >= prec1):
                    process_operation()
                op_stack.append(token)
        while op_stack:
            process_operation()
        return output_values[0] if output_values else None
if __name__ == '__main__':
    parser = OperatorPrecedence()
    expression1 = "10 + 5 * 2"
    result1 = parser.evaluate_expression(expression1)
    print(f"Expression: {expression1}")
    print(f"Result: {result1}")
    print("-" * 20)
    expression2 = "10 & 5 | 3"
    result2 = parser.evaluate_expression(expression2)
    print(f"Expression: {expression2}")
    print(f"Result: {result2}")
    print("-" * 20)
    expression3 = "10 + 2 * 3 - 1"
    result3 = parser.evaluate_expression(expression3)
    print(f"Expression: {expression3}")
    print(f"Result: {result3}")
    print("-" * 20)
    expression4 = "10 << 2"
    result4 = parser.evaluate_expression(expression4)
    print(f"Expression: {expression4}")
    print(f"Result: {result4}")
    print("-" * 20)
    expression5 = "100 / 5 + 20 % 3"
    result5 = parser.evaluate_expression(expression5)
    print(f"Expression: {expression5}")
    print(f"Result: {result5}")
    print("-" * 20)