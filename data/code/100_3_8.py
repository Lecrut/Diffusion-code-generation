class LogicChecker:
    def evaluate(self, bool_list):
        return all(bool_list)

if __name__ == '__main__':
    checker = LogicChecker()
    result = checker.evaluate([True, True, True])
    print(result)