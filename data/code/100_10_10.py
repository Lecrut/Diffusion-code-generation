class LogicChecker:
    def evaluate(self, expression):
        return eval(expression)

if __name__ == '__main__':
    checker = LogicChecker()
    result = checker.evaluate('2 + 3 * 4')
    print(result)