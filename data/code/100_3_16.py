class LogicChecker:
    def evaluate(self, values):
        return all(values)

if __name__ == '__main__':
    checker = LogicChecker()
    print(checker.evaluate([True, True, True]))
    print(checker.evaluate([True, False, True]))