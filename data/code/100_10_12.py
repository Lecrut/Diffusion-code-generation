class LogicChecker:
    def evaluate(self, expression):
        return eval(expression)

if __name__ == '__main__':
    checker = LogicChecker()
    result = checker.evaluate('3 + 5 * 2')
    print(result)