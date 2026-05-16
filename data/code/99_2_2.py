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
            '^': 3,               
            '<<': 4,                      
            '>>': 4,                       
            '~': 5,                
            '==': 6,            
            '!=': 6,
            '<=': 6,
            '>=': 6
        }
        def get_precedence(op):
            return precedence.get(op, -1)
        def apply_op(op, b, a):
            if op == '+': return a + b
            if op == '-': return a - b
            if op == '*': return a * b
            if op == '/':
                if b == 0: raise ZeroDivisionError("Division by zero")
                return a // b if a % b == 0 else a / b
            if op == '%': return a % b
            if op == '&': return a & b
            if op == '|': return a | b
            if op == '^': return a ^ b
            if op == '<<': return a << b
            if op == '>>': return a >> b
            if op == '~': return ~a
            if op == '==': return a == b
            if op == '!=': return a != b
            if op == '<=': return a <= b
            if op == '>=': return a >= b
            raise ValueError(f"Unknown operator: {op}")
        def evaluate_tokens(tokens):
            if not tokens:
                return None
            values = []
            ops = []
            for token in tokens:
                if token.isdigit() or (token.startswith('-') and token[1:].isdigit()):
                    values.append(float(token))
                elif token == '(':
                    values.append(token)
                elif token == ')':
                    balance = 1
                    sub_expression = []
                    for i in range(len(values) - 1):
                        if values[i] == '(': balance += 1
                        elif values[i] == ')': balance -= 1
                        if balance == 0:
                            sub_expression = values[i+1:i]
                            break
                    if balance != 0:
                        raise ValueError("Mismatched parentheses")
                    pass
                elif token in precedence:
                    ops.append(token)
                else:
                    raise ValueError(f"Invalid token encountered: {token}")
            output_queue = []
            operator_stack = []
            for token in tokens:
                if token.isdigit() or (token.startswith('-') and token[1:].isdigit()):
                    output_queue.append(token)
                elif token == '(':
                    operator_stack.append(token)
                elif token == ')':
                    while operator_stack and operator_stack[-1] != '(':
                        op = operator_stack.pop()
                        val2 = output_queue.pop()
                        val1 = output_queue.pop()
                        output_queue.append(apply_op(op, val2, val1))
                    if not operator_stack or operator_stack[-1] != '(':
                        raise ValueError("Mismatched parentheses")
                    operator_stack.pop()
                elif token in precedence:
                    while (operator_stack and operator_stack[-1] != '(' and 
                           get_precedence(operator_stack[-1]) >= get_precedence(token)):
                        op = operator_stack.pop()
                        val2 = output_queue.pop()
                        val1 = output_queue.pop()
                        output_queue.append(apply_op(op, val2, val1))
                    operator_stack.append(token)
                else:
                    raise ValueError(f"Unknown token: {token}")
            while operator_stack:
                op = operator_stack.pop()
                if op == '(':
                    raise ValueError("Mismatched parentheses")
                val2 = output_queue.pop()
                val1 = output_queue.pop()
                output_queue.append(apply_op(op, val2, val1))
            return output_queue[0] if output_queue else None
        sorted_tokens = []
        for token in tokens:
            if token in precedence:
                sorted_tokens.append((get_precedence(token), token))
            else:
                sorted_tokens.append((100, token))                                            
        sorted_tokens.sort(key=lambda x: (x[0], x[1]))
        return [t[1] for t in sorted_tokens]
if __name__ == '__main__':
    parser = OperatorPrecedence()
    expression1 = "10 + 5 * 2 & 3"
    tokens1 = parser.parse_expression(expression1)
    sorted_ops1 = parser.apply_precedence(tokens1)
    print(f"Expression: {expression1}")
    print(f"Tokens: {tokens1}")
    print(f"Sorted Operations (Precedence Order): {sorted_ops1}\n")
    expression2 = "(10 << 2) + 5 * (8 | 1)"
    tokens2 = parser.parse_expression(expression2)
    sorted_ops2 = parser.apply_precedence(tokens2)
    print(f"Expression: {expression2}")
    print(f"Tokens: {tokens2}")
    print(f"Sorted Operations (Precedence Order): {sorted_ops2}\n")
    expression3 = "10 > 5 & 2 == 2"
    tokens3 = parser.parse_expression(expression3)
    sorted_ops3 = parser.apply_precedence(tokens3)
    print(f"Expression: {expression3}")
    print(f"Tokens: {tokens3}")
    print(f"Sorted Operations (Precedence Order): {sorted_ops3}\n")