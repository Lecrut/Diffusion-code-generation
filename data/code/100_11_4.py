class LogicChecker:
    def evaluate_expression(self, expression: str, variables: dict) -> bool:
        import re
        def evaluate_token(token, vars):
            if token.isdigit() or (token.startswith('-') and token[1:].isdigit()):
                return float(token)
            return vars.get(token, 0)
        tokens = re.findall(r'[a-zA-Z_()]|[-+*/=]|[\d.]+', expression)
        if not tokens:
            raise ValueError("Empty expression")
        stack = []
        operators = []
        for token in tokens:
            if token.replace('.', '', 1).isdigit():
                stack.append(float(token))
            elif token in ['(', '+', '-', '*', '/', '=']:
                if token in ['+', '-', '*', '/']:
                    operators.append(token)
                elif token == '(':
                    stack.append(token)
                elif token == '=':
                    if len(stack) < 2:
                        raise ValueError("Syntax error: '=' requires two operands")
                    op = operators.pop()
                    right = stack.pop()
                    left = stack.pop()
                    if op == '+':
                        result = left + right
                    elif op == '-':
                        result = left - right
                    elif op == '*':
                        result = left * right
                    elif op == '/':
                        if right == 0:
                            raise ZeroDivisionError("Division by zero")
                        result = left / right
                    stack.append(result)
                else:
                    pass
            else:
                if token in variables:
                    stack.append(variables[token])
                else:
                    raise NameError(f"Undefined variable: {token}")
        if not stack:
            raise ValueError("Invalid expression structure")
        if len(stack) != 1:
            raise ValueError("Invalid expression structure or unmatched operators")
        result = stack[0]
        if isinstance(result, (int, float)):
            return bool(result)
        return bool(result)
if __name__ == '__main__':
    checker = LogicChecker()
    sample_variables = {
        "A": True,
        "B": False,
        "C": 10,
        "X": 5.5
    }
    expression1 = "A + B * 2"
    try:
        result1 = checker.evaluate_expression(expression1, sample_variables)
        print(f"Expression: '{expression1}', Result: {result1}")
    except Exception as e:
        print(f"Error evaluating '{expression1}': {e}")
    expression2 = "(C > 5) AND (A == True)"                                                                                               
    expression3 = "A * (C / 2)"
    try:
        result3 = checker.evaluate_expression(expression3, sample_variables)
        print(f"Expression: '{expression3}', Result: {result3}")
    except Exception as e:
        print(f"Error evaluating '{expression3}': {e}")
    expression4 = "X > 0"                                                                                                           
    try:
        expression5 = "A > 0"                                         
        print(f"Expression: '{expression5}', Result: {checker.evaluate_expression(expression5, sample_variables)}")
    except Exception as e:
        print(f"Error evaluating '{expression5}': {e}")
    expression6 = "A * 2"
    try:
        result6 = checker.evaluate_expression(expression6, sample_variables)
        print(f"Expression: '{expression6}', Result: {result6}")
    except Exception as e:
        print(f"Error evaluating '{expression6}': {e}")
    expression7 = "A + B"
    try:
        result7 = checker.evaluate_expression(expression7, sample_variables)
        print(f"Expression: '{expression7}', Result: {result7}")
    except Exception as e:
        print(f"Error evaluating '{expression7}': {e}")