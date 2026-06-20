class LogicChecker:
    def evaluate(self, bool_list):
        return all(bool_list)

if __name__ == '__main__':
    checker = LogicChecker()
    print(checker.evaluate([True, True, True]))
    print(checker.evaluate([True, False, True]))