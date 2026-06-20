class BooleanLogic:
    TRUE = True
    FALSE = False

    def __init__(self, value):
        self.value = bool(value)

    @staticmethod
    def and_(A, B):
        return BooleanLogic(A.value and B.value)

    @staticmethod
    def or_(A, B):
        return BooleanLogic(A.value or B.value)

    @staticmethod
    def not_(A):
        return BooleanLogic(not A.value)
if __name__ == '__main__':
    a = BooleanLogic(True)
    b = BooleanLogic(False)
    result_and = BooleanLogic.and_(a, b).value
    result_or = BooleanLogic.or_(a, b).value
    result_not = BooleanLogic.not_(b).value
    print(result_and)
    print(result_or)
    print(result_not)