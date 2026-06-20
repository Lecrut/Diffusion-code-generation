class LogicOperations:
    TRUE = 1
    FALSE = 0

    @staticmethod
    def logical_and(a: bool, b: bool) -> bool:
        return a & b

    @staticmethod
    def logical_or(a: bool, b: bool) -> bool:
        return a | b

    @staticmethod
    def logical_not(a: bool) -> bool:
        return not a
if __name__ == '__main__':
    logic = LogicOperations()
    print(logic.logical_and(True, False))
    print(logic.logical_or(False, True))
    print(logic.logical_not(True))