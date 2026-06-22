class ConditionChecker:
    MIN_VALUE = 0
    MAX_VALUE = 100
    MODULO = 2

    @staticmethod
    def is_valid(value):
        return ConditionChecker.MIN_VALUE < value < ConditionChecker.MAX_VALUE and value % ConditionChecker.MODULO == 0

    @classmethod
    def check_all(cls, a, b, c):
        return cls.is_valid(a) and cls.is_valid(b) and cls.is_valid(c)

if __name__ == '__main__':
    print(ConditionChecker.check_all(2, 4, 6))
    print(ConditionChecker.check_all(2, 4, 102))
    print(ConditionChecker.check_all(2, 3, 4))
    print(ConditionChecker.check_all(-2, 4, 6))