class LogicOperations:
    @staticmethod
    def check_or_condition(a: bool, b: bool) -> bool:
        return a or b

if __name__ == '__main__':
    logic_ops = LogicOperations()
    print(logic_ops.check_or_condition(True, False))
    print(logic_ops.check_or_condition(False, True))
    print(logic_ops.check_or_condition(True, True))
    print(logic_ops.check_or_condition(False, False))