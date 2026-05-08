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
    def apply_precedence(self, tokens):
        if not tokens:
            return []
        precedence = {
            '(': 0, ')': 0,
            '**': 3,                  
            '*': 2, '/': 2, '%': 2,
            '+': 1, '-': 1,
            '&': 3,               
            '|': 3,              
            '^': 4,               
            '<<': 5,              
            '>>': 5,               
            '~': 4,               
            '==': 6,            
            '!=': 6,
            '<=': 6,
            '>=': 6
        }
        output = []
        stack = []
        def process_operation(op, values):
            if op in ('+', '-', '*', '/', '%', '&', '|', '^'):
                if len(values) < 2:
                    raise ValueError("Insufficient operands for binary operator")
                op1 = values.pop()
                op2 = values.pop()
                if op == '+':
                    result = op1 + op2
                elif op == '-':
                    result = op1 - op2
                elif op == '*':
                    result = op1 * op2
                elif op == '/':
                    result = op1 / op2
                elif op == '%':
                    result = op1 % op2
                elif op == '&':
                    result = op1 & op2
                elif op == '|':
                    result = op1 | op2
                elif op == '^':
                    result = op1 ^ op2
                values.append(result)
            elif op == '**':
                if len(values) < 2:
                    raise ValueError("Insufficient operands for exponentiation")
                op1 = values.pop()
                op2 = values.pop()
                result = op1 ** op2
                values.append(result)
            elif op == '<<':
                if len(values) < 2:
                    raise ValueError("Insufficient operands for left shift")
                op1 = values.pop()
                op2 = values.pop()
                result = op1 << op2
                values.append(result)
            elif op == '>>':
                if len(values) < 2:
                    raise ValueError("Insufficient operands for right shift")
                op1 = values.pop()
                op2 = values.pop()
                result = op1 >> op2
                values.append(result)
            else:
                raise ValueError(f"Unknown operator: {op}")
        for token in tokens:
            if token.isdigit() or (token.startswith('-') and token[1:].isdigit()):
                stack.append(float(token))
            elif token == '(':
                stack.append(token)
            elif token == ')':
                if len(stack) < 2:
                    raise ValueError("Mismatched parentheses")
                result = []
                while stack[-1] != '(':
                    op = stack.pop()
                    operands = []
                    while op != '(':
                        operands.append(stack.pop())
                        op = stack.pop()
                    if len(operands) > 0:
                        pass                                                                             
                    stack.append(operands.pop())                       
                if stack and stack[-1] == '(':
                    stack.pop()              
            elif token in precedence:
                while (stack and stack[-1] != '(' and 
                       precedence.get(stack[-1], -1) >= precedence[token]):
                    op = stack.pop()
                    if len(stack) > 0:
                        pass
                stack.append(token)
            else:
                pass
        if stack:
            while stack:
                output.append(stack.pop())
        return output
if __name__ == '__main__':
    parser = OperatorPrecedence()
    expression1 = "10 + 5 * 2"
    tokens1 = parser.parse_expression(expression1)
    print(f"Expression: {expression1}")
    print(f"Tokens: {tokens1}")
    expression2 = "10 + 5 * 2"
    tokens2 = parser.parse_expression(expression2)
    print(f"\nExpression: {expression2}")
    print(f"Tokens: {tokens2}")
    expression3 = "10 & 5 | 3"
    tokens3 = parser.parse_expression(expression3)
    print(f"\nExpression: {expression3}")
    print(f"Tokens: {tokens3}")
    expression4 = "(10 + 5) * 2"
    tokens4 = parser.parse_expression(expression4)
    print(f"\nExpression: {expression4}")
    print(f"Tokens: {tokens4}")