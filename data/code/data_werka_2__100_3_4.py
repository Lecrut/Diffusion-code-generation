class LogicChecker:
    def evaluate(self, values):
        return all(values)

if __name__ == '__main__':
    checker = LogicChecker()
    result = checker.evaluate([True, True, True])
    print(result)