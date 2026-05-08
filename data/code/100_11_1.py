class LogicChecker:
    def evaluate(self, expression: str, variables: dict) -> bool:
        import re
        def substitute(match):
            var_name = match.group(1)
            if var_name in variables:
                return str(variables[var_name])
            return match.group(0)
        tokens = re.findall(r'\(|\)|\w+|\+|\-|\*|\/|=', expression)
        if not tokens:
            raise ValueError("Empty expression")
        result_stack = []
        operator_stack = []
        def apply_op():
            op = operator_stack.pop()
            right = result_stack.pop()
            left = result_stack.pop()
            if op == '+':
                result_stack.append(left + right)
            elif op == '-':
                result_stack.append(left - right)
            elif op == '*':
                result_stack.append(left * right)
            elif op == '/':
                if right == 0:
                    raise ZeroDivisionError("Division by zero")
                result_stack.append(left / right)
            else:
                raise ValueError(f"Unknown operator: {op}")
        for token in tokens:
            if token.replace('.', '', 1).isdigit() or (token.startswith('-') and token[1:].replace('.', '', 1).isdigit()):
                result_stack.append(float(token))
            elif token == '(':
                operator_stack.append(token)
            elif token == ')':
                while operator_stack[-1] != '(':
                    apply_op()
                operator_stack.pop()
            elif token in ('+', '-', '*', '/'):
                operator_stack.append(token)
            elif re.match(r'^\w+$', token):
                result_stack.append(variables.get(token, 0))
            else:
                raise ValueError(f"Invalid token: {token}")
        while operator_stack:
            apply_op()
        if len(result_stack) == 1:
            return True
        raise ValueError("Malformed expression")
if __name__ == '__main__':
    checker = LogicChecker()
    variables1 = {
        "a": 10,
        "b": 5
    }
    expression1 = "(a + b) * 2"
    try:
        result1 = checker.evaluate(expression1, variables1)
        print(f"Expression: {expression1}, Variables: {variables1}")
        print(f"Result: {result1}")
    except Exception as e:
        print(f"Error evaluating '{expression1}': {e}")
    print("-" * 20)
    variables2 = {
        "x": 3,
        "y": 4
    }
    expression2 = "x * (y - 1) / 2"
    try:
        result2 = checker.evaluate(expression2, variables2)
        print(f"Expression: {expression2}, Variables: {variables2}")
        print(f"Result: {result2}")
    except Exception as e:
        print(f"Error evaluating '{expression2}': {e}")
    print("-" * 20)
    variables3 = {"p": 1}
    expression3 = "p"
    try:
        result3 = checker.evaluate(expression3, variables3)
        print(f"Expression: {expression3}, Variables: {variables3}")
        print(f"Result: {result3}")
    except Exception as e:
        print(f"Error evaluating '{expression3}': {e}")
    print("-" * 20)
    variables4 = {"A": 1, "B": 1}
    expression4 = "(A > 0) and (B == 1)"                                                       
    try:
        result4 = checker.evaluate("A + B", variables4)
        print(f"Expression: 'A + B', Variables: {variables4}")
        print(f"Result: {result4}")
    except Exception as e:
        print(f"Error evaluating '{expression4}': {e}")