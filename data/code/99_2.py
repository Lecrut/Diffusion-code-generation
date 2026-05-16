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
            if char.isalnum() or char in '+-*/&|^!(){}=':
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
            '&': 2,
            '|': 2,
            '^': 2,
            '+': 1,
            '-': 1,
            '*': 3,
            '/': 3,
            '==': 4,
            '!=': 4,
            '<=': 4,
            '>=': 4,
            '===': 5,
            '<<': 5,
            '>>': 5,
        }
        output = []
        stack = []
        operators = []
        def process_op(op, values):
            if op in precedence:
                pre = precedence[op]
                while stack and stack[-1] != '(':
                    top = stack[-1]
                    if top in precedence:
                        stack.pop()
                        values.append(top)
                        operators.append(top)
                    else:
                        break
                if stack and stack[-1] == '(':
                    stack.pop()
                if op not in ['(', ')']:
                    stack.append(op)
            else:
                stack.append(op)
        for token in tokens:
            if token.isdigit() or (token.startswith('-') and token[1:].isdigit()):
                stack.append(token)
            elif token == '(':
                stack.append(token)
            elif token == ')':
                while stack and stack[-1] != '(':
                    output.append(stack.pop())
                if stack and stack[-1] == '(':
                    stack.pop()
            elif token in precedence:
                process_op(token, output)
            else:
                output.append(token)
        while stack:
            if stack[-1] != '(':
                output.append(stack.pop())
            else:
                stack.pop()
        return output
if __name__ == '__main__':
    parser = OperatorPrecedence()
    expression1 = "10 + 5 * 2"
    tokens1 = parser.parse_expression(expression1)
    result1 = parser.apply_precedence(tokens1)
    print(f"Expression: {expression1}")
    print(f"Tokens: {tokens1}")
    print(f"Result: {result1}\n")
    expression2 = "(10 + 5) * 2"
    tokens2 = parser.parse_expression(expression2)
    result2 = parser.apply_precedence(tokens2)
    print(f"Expression: {expression2}")
    print(f"Tokens: {tokens2}")
    print(f"Result: {result2}\n")
    expression3 = "10 & 5 | 3"
    tokens3 = parser.parse_expression(expression3)
    result3 = parser.apply_precedence(tokens3)
    print(f"Expression: {expression3}")
    print(f"Tokens: {tokens3}")
    print(f"Result: {result3}\n")
    expression4 = "10 + 5 * 2 - 1"
    tokens4 = parser.parse_expression(expression4)
    result4 = parser.apply_precedence(tokens4)
    print(f"Expression: {expression4}")
    print(f"Tokens: {tokens4}")
    print(f"Result: {result4}\n")
    expression5 = "10 << 2"
    tokens5 = parser.parse_expression(expression5)
    result5 = parser.apply_precedence(tokens5)
    print(f"Expression: {expression5}")
    print(f"Tokens: {tokens5}")
    print(f"Result: {result5}\n")