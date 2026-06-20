class BooleanLogic:
    TRUE = True
    FALSE = False

    def __init__(self, value):
        self.value = bool(value)

    @staticmethod
    def and_operation(a: 'BooleanLogic', b: 'BooleanLogic') -> 'BooleanLogic':
        return BooleanLogic(a.value and b.value)

    @staticmethod
    def or_operation(a: 'BooleanLogic', b: 'BooleanLogic') -> 'BooleanLogic':
        return BooleanLogic(a.value or b.value)

    @staticmethod
    def not_operation(a: 'BooleanLogic') -> 'BooleanLogic':
        return BooleanLogic(not a.value)
if __name__ == '__main__':
    a = BooleanLogic(True)
    b = BooleanLogic(False)
    print(BooleanLogic.and_operation(a, b).value)
    print(BooleanLogic.or_operation(a, b).value)
    print(BooleanLogic.not_operation(b).value)