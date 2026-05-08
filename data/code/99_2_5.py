class OperatorPrecedence:
    def parse_expression(self, expression):
        tokens = expression.split()
        if not tokens:
            return []
        output = []
        operators = []
        for token in tokens:
            if token.isdigit() or (token.startswith('-') and token[1:].isdigit()):
                output.append(token)
            elif token in ['+', '-', '*', '/', '^', '&', '|', '^']:
                operators.append(token)
            else:
                output.append(token)
        return output, operators
    def evaluate_expression(self, expression):
        output, operators = self.parse_expression(expression)
        if not output:
            return None
        values = []
        ops = []
        for token in output:
            if token.isdigit() or (token.startswith('-') and token[1:].isdigit()):
                values.append(float(token))
            elif token in ['+', '-', '*', '/', '^', '&', '|']:
                ops.append(token)
        if not values:
            return None
        i = 0
        while i < len(ops):
            op = ops[i]
            if i + 1 < len(values):
                operand1 = values[i]
                operand2 = values[i+1]
                values.pop()
                values.append(operand2)
                if op == '+':
                    result = operand1 + operand2
                elif op == '-':
                    result = operand1 - operand2
                elif op == '*':
                    result = operand1 * operand2
                elif op == '/':
                    if operand2 == 0:
                        raise ZeroDivisionError("Division by zero")
                    result = operand1 / operand2
                elif op == '^':
                    result = operand1 ** operand2
                elif op == '&':
                    result = operand1 & operand2
                elif op == '|':
                    result = operand1 | operand2
                else:
                    raise ValueError(f"Unknown operator: {op}")
                values.pop()
                values.append(result)
            i += 1
        if len(values) == 1:
            return values[0]
        else:
            raise ValueError("Invalid expression structure")
if __name__ == '__main__':
    parser = OperatorPrecedence()
    expression1 = "10 + 5 * 2"
    try:
        result1 = parser.evaluate_expression(expression1)
        print(f"Expression: {expression1}")
        print(f"Result: {result1}")
    except Exception as e:
        print(f"Error processing {expression1}: {e}")
    print("-" * 20)
    expression2 = "10 + 5 & 3"                                                                              
    try:
        expression2_arithmetic = "10 + 5 * 2"
        result2_arithmetic = parser.evaluate_expression(expression2_arithmetic)
        print(f"Expression: {expression2_arithmetic}")
        print(f"Result: {result2_arithmetic}")
    except Exception as e:
        print(f"Error processing {expression2_arithmetic}: {e}")
    print("-" * 20)
    expression3 = "10 + 5 * 2"
    try:
        result3 = parser.evaluate_expression(expression3)
        print(f"Expression: {expression3}")
        print(f"Result: {result3}")
    except Exception as e:
        print(f"Error processing {expression3}: {e}")