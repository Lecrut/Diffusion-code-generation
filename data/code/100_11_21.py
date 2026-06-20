class LogicChecker:
    TRUE = True
    FALSE = False

    @staticmethod
    def all_true(values):
        return all((value == LogicChecker.TRUE for value in values))

    @staticmethod
    def all_false(values):
        return all((value == LogicChecker.FALSE for value in values))
if __name__ == '__main__':
    sample_values = [True, True, True]
    print(LogicChecker.all_true(sample_values))
    sample_values = [False, False, False]
    print(LogicChecker.all_false(sample_values))