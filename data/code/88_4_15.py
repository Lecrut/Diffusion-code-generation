class BooleanLogic:
    @staticmethod
    def and_operation(val1: bool, val2: bool) -> bool:
        return val1 and val2

if __name__ == '__main__':
    print(BooleanLogic.and_operation(True, True))
    print(BooleanLogic.and_operation(True, False))
    print(BooleanLogic.and_operation(False, True))
    print(BooleanLogic.and_operation(False, False))