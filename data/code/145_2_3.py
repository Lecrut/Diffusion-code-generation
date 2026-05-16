class BooleanTester:
    def evaluate_nested(self, expression):
        if isinstance(expression, str):
            expression = expression.replace('and', '&&').replace('or', '||').replace('not', '!')
        tokens = expression.split()
        if not tokens:
            return False
        result_stack = []
        operator_stack = []
        for token in tokens:
            if token in ('True', 'False'):
                result_stack.append(token == 'True')
            elif token == '(':
                operator_stack.append('(')
            elif token == ')':
                while operator_stack and operator_stack[-1] != '(':
                    result_stack.append(operator_stack.pop())
                if operator_stack and operator_stack[-1] == '(':
                    operator_stack.pop()
            elif token in ('&&', '||', '!'):
                operator_stack.append(token)
            else:
                try:
                    value = bool(token)
                    result_stack.append(value)
                except ValueError:
                    raise ValueError(f"Invalid token encountered: {token}")
        final_result = []
        while operator_stack:
            op = operator_stack.pop()
            if op == '(':
                continue
            if op == '!':
                if not result_stack:
                    raise ValueError("Syntax error: '!' requires an operand")
                operand = result_stack.pop()
                result_stack.append(not operand)
            elif op in ('&&', '||'):
                if len(result_stack) < 2:
                    raise ValueError(f"Syntax error: Binary operator {op} requires two operands")
                right = result_stack.pop()
                left = result_stack.pop()
                if op == '&&':
                    result_stack.append(left and right)
                elif op == '||':
                    result_stack.append(left or right)
            else:
                raise ValueError(f"Unknown operator: {op}")
        if len(result_stack) != 1:
            raise ValueError("Malformed expression structure")
        return result_stack[0]
if __name__ == '__main__':
    tester = BooleanTester()
    expr1 = "True && False"
    result1 = tester.evaluate_nested(expr1)
    print(f"Expression: '{expr1}', Result: {result1}")
    expr2 = "(True || False) && not False"
    result2 = tester.evaluate_nested(expr2)
    print(f"Expression: '{expr2}', Result: {result2}")
    expr3 = "True || (False && not True)"
    result3 = tester.evaluate_nested(expr3)
    print(f"Expression: '{expr3}', Result: {result3}")
    expr4 = "True or False and True"
    result4 = tester.evaluate_nested(expr4)
    print(f"Expression: '{expr4}', Result: {result4}")
    expr5 = "(True && False) || (!False)"
    result5 = tester.evaluate_nested(expr5)
    print(f"Expression: '{expr5}', Result: {result5}")