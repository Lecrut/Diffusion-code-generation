class LogicChecker:
    TRUE = True
    FALSE = False

    @staticmethod
    def all_true(values: list) -> bool:
        return all(value == LogicChecker.TRUE for value in values)

    @staticmethod
    def all_false(values: list) -> bool:
        return all(value == LogicChecker.FALSE for value in values)

if __name__ == '__main__':
    print(LogicChecker.all_true([True, True, True]))
    print(LogicChecker.all_false([False, False, False]))
    print(LogicChecker.all_true([True, False, True]))
    print(LogicChecker.all_false([True, False, False]))