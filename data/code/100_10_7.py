class LogicChecker:

    def evaluate_expression(self, expression):
        operators = {'and': lambda x, y: x and y, 'or': lambda x, y: x or y, 'not': lambda x: not x}
        tokens = expression.split()
        stack = []
        for token in tokens:
            if token.isdigit():
                stack.append(int(token))
            elif token in operators:
                right = stack.pop()
                left = stack.pop()
                result = operators[token](left, right)
                stack.append(result)
        return stack[0]
if __name__ == '__main__':
    checker = LogicChecker()
    print(checker.evaluate_expression('1 2 +'))
    print(checker.evaluate_expression('3 4 *'))
    print(checker.evaluate_expression('5 2 -'))
    print(checker.evaluate_expression('6 3 /'))