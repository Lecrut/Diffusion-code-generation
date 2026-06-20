class LogicChecker:
    def evaluate_expression(self, expression):
        allowed_operators = {
            'and': lambda x, y: x and y,
            'or': lambda x, y: x or y,
            'not': lambda x: not x
        }
        
        tokens = expression.split()
        stack = []
        
        for token in tokens:
            if token.isdigit():
                stack.append(int(token))
            elif token == 'True':
                stack.append(True)
            elif token == 'False':
                stack.append(False)
            elif token in allowed_operators:
                right = stack.pop()
                left = stack.pop()
                result = allowed_operators[token](left, right)
                stack.append(result)
        
        return stack[0]

if __name__ == '__main__':
    checker = LogicChecker()
    expressions_to_test = [
        "True and False",
        "not True",
        "5 > 3"
    ]
    
    for expr in expressions_to_test:
        print(f"{expr} = {checker.evaluate_expression(expr)}")