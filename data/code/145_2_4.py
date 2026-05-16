class BooleanTester:
    def evaluate_nested(self, expression):
        if isinstance(expression, str):
            expression = expression.replace('and', '&&').replace('or', '||').replace('not', '!')
        tokens = expression.split()
        if not tokens:
            return False
        result_stack = []
        operator_stack = []
        def apply_op():
            op = operator_stack.pop()
            if op == 'NOT':
                operand = result_stack.pop()
                result_stack.append(not operand)
            elif op == 'AND':
                right = result_stack.pop()
                left = result_stack.pop()
                result_stack.append(left and right)
            elif op == 'OR':
                right = result_stack.pop()
                left = result_stack.pop()
                result_stack.append(left or right)
        for token in tokens:
            if token == 'True':
                result_stack.append(True)
            elif token == 'False':
                result_stack.append(False)
            elif token in ('and', 'or', 'not'):
                operator_stack.append(token)
            else:
                try:
                    value = bool(token)
                    result_stack.append(value)
                except ValueError:
                    raise ValueError(f"Invalid boolean token: {token}")
            if operator_stack and operator_stack[-1] in ('and', 'or', 'not'):
                apply_op()
        if result_stack:
            return result_stack[0]
        return False
if __name__ == '__main__':
    tester = BooleanTester()
    expr1 = "True and False"
    result1 = tester.evaluate_nested(expr1)
    print(f"Expression: '{expr1}', Result: {result1}")
    expr2 = "True or (False and True)"
    result2 = tester.evaluate_nested(expr2)
    print(f"Expression: '{expr2}', Result: {result2}")
    expr3 = "not True and False"
    result3 = tester.evaluate_nested(expr3)
    print(f"Expression: '{expr3}', Result: {result3}")
    expr4 = "True or False and True"
    result4 = tester.evaluate_nested(expr4)
    print(f"Expression: '{expr4}', Result: {result4}")
    expr5 = "False or True"
    result5 = tester.evaluate_nested(expr5)
    print(f"Expression: '{expr5}', Result: {result5}")
    expr6 = "not True and False or True"
    result6 = tester.evaluate_nested(expr6)
    print(f"Expression: '{expr6}', Result: {result6}")