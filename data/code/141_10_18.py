class LogicOperations:
    def logical_and(self, a: bool, b: bool) -> bool:
        return a & b

    def logical_or(self, a: bool, b: bool) -> bool:
        return a | b

    def logical_not(self, a: bool) -> bool:
        return not a

if __name__ == '__main__':
    logic = LogicOperations()
    result_and = logic.logical_and(True, False)
    result_or = logic.logical_or(False, True)
    result_not = logic.logical_not(True)
    print(result_and)
    print(result_or)
    print(result_not)